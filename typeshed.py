from dataclasses import dataclass, field
from typing import List, Set, Dict, Callable, Optional

from lines import Lines

__author__ = "Howard C Lovatt"
__copyright__ = "Howard C Lovatt, 2020 onwards."
__license__ = "MIT https://opensource.org/licenses/MIT (as used by MicroPython)."
__version__ = "1.0.0"


@dataclass
class Typeshed:
    """
    Converts `.rst` documentation files into `.pyi` typeshed stub interfaces.
    The conversion process is declarative and after declaring the module follows whatever order the `.rst` file is in:

      1. Declare the `module`.
      2. Declare the `def_`s in the module.
      3. Declare the `class_`s in the module.
      4. Declare the `def_`s inside the classes.
      5. `.rst` files might at any point contain `extra_notes`, `constants`, and multiple `defs` in one block.

    In addition to the above declarative conversions you can:

      1. `preview` the conversions so far (useful for debugging).
      2. `write` the finished conversion to the `.pyi` file (the point of the exercise!).

    A simple example of using `Typeshed` is `uarray.py` and a complicated example is `pyb.py`.
    """

    name: str
    output_dir: str
    input_base_url: str = r'https://raw.githubusercontent.com/micropython/micropython/master/docs/library/'
    typeshed: List[str] = field(default_factory=list)
    lines: Lines = Lines()
    _last_class_index: int = 0
    _last_line_index: int = 0

    _title_underline: Set[str] = field(default_factory=lambda: set('='))
    _header_underline: Set[str] = field(default_factory=lambda: set('-'))
    _synopsis: str = '   :synopsis: '
    _definitions: str = '.. '
    _note: str = '.. note::'

    def is_last(self, line: str, end: str) -> bool:
        """
        Many of the parsing functions have an end argument, this function is used for end testing.
        If `line` is `end` then the line is pushed-back and `True` returned, else no push-back and `False`.
        Testing for `end` is slightly more complicated than simply comparing lines:

          1. White space is stripped from the start to account for indentation.
          2. If the line starts with definition `self._note` then it is not an end line
          (this is because the default end line is `self._definitions`,
          but the note definition is part of the current parsing unit - its a note!).
          3. `end` is compared to the start of `line` (to allow partial matches).

        :param line: The line to be tested.
        :param end: The line to test for.
        :return: True if `line` is `end` line.
        """
        s_line = line.lstrip()
        if not s_line.startswith(self._note) and s_line.startswith(end):
            self.lines.push_line(line)
            return True
        return False

    def consume_line(self, test: Callable[[str], bool], *, msg: str, and_preceding_lines: bool = False) -> None:
        if and_preceding_lines:
            for line in self.lines:
                if test(line):
                    break
            else:
                assert False, f'Expected {msg}, but reached end-of-file before finding it!'
        else:
            line = next(self.lines)
            assert test(line), f'Expected {msg}, got `{line}`!'

    def consume_title_line(self, *, and_preceding_lines: bool = False) -> None:
        self.consume_line(
            lambda s: set(s).issubset(self._title_underline),
            msg='a title-underline line',
            and_preceding_lines=and_preceding_lines
        )

    def consume_header_line(self, *, and_preceding_lines: bool = False) -> None:
        self.consume_line(
            lambda s: set(s).issubset(self._header_underline),
            msg='a header-underline line',
            and_preceding_lines=and_preceding_lines
        )

    def consume_blank_line(self, *, and_preceding_lines: bool = False) -> None:
        self.consume_line(lambda s: not s.strip(), msg='a blank line', and_preceding_lines=and_preceding_lines)

    def consume_name_line(self, name: str, *, and_preceding_lines: bool = False) -> None:
        self.consume_line(lambda s: s.startswith(name), msg=name, and_preceding_lines=and_preceding_lines)

    def module(self, *, old: str, new: Optional[str] = None, post_doc: str = '', end: str = _definitions) -> None:
        url = self.input_base_url + self.name + '.rst'
        self.lines.push_url(url)
        for line in self.lines:
            if line.startswith(self._synopsis):
                break
        else:
            assert False, f'Expected synopsis of `{old}`, but did not find it!'
        if new is None:
            new = old
        self.typeshed.append(f'''"""
{new}

Descriptions taken from 
`{url}`, etc.
"""

__author__ = "Howard C Lovatt"
__copyright__ = "Howard C Lovatt, 2020 onwards."
__license__ = "MIT https://opensource.org/licenses/MIT (as used by MicroPython)."
__version__ = "0.1.0"


{post_doc}
'''
                             )
        for line in self.lines:
            if self.is_last(line, end):  # Skip over lines to end of synopsis.
                break

    def class_(self, *, old: str, post_doc: str = '') -> None:
        self._last_class_index = len(self.typeshed)
        self._last_line_index = -(len(post_doc) + 7)
        for line in self.lines:
            if line.lstrip().startswith(old):
                url = self.input_base_url + old.strip()
                self.lines.push_url(url)
                break
        else:
            assert False, f'Did not find: `{old}`!'
        rst = old[old.find('.') + 1:]
        class_name = rst[:rst.find('.')]
        for line in self.lines:
            if line and set(line).issubset(self._title_underline):
                break
        self.consume_blank_line()
        doc = []
        for doc_line in self.lines:
            if doc_line and set(doc_line).issubset(self._header_underline):
                assert doc[-1].strip(), f'Expected a non-blank line, got blank!'  # Remove header.
                del doc[-1]
                assert not doc[-1].strip(), f'Expected a blank line, got `{doc[-1]}`!'
                del doc[-1]
                break
            else:
                doc.append(f'   {doc_line}\n')
        else:
            assert doc, 'Did not find any class documentation.'
        self.consume_blank_line()
        self.typeshed.append(f'''
class {class_name}: 
   """
{''.join(doc).rstrip()}
   """{post_doc}
'''
                             )

    def def_(self, *, old: str, new: str, indent: int = 0, end: str = _definitions) -> None:
        self.consume_name_line(old, and_preceding_lines=True)
        self.consume_line(
            lambda s: not s.strip() or s.startswith('   :noindex:'),
            msg='a blank line or `:noindex:` line'
        )
        in_str = indent * ' '
        return_plus_in_str = '\n' + in_str
        doc = []
        for doc_line in self.lines:
            if self.is_last(doc_line, end):
                break
            if doc_line and set(doc_line).issubset(self._header_underline):
                assert doc[-1], f'Expected heading, got blank line!'
                del doc[-1]  # Remove heading text (which is followed by detected underline).
                assert not doc[-1].strip(), f'Expected blank line, got `{doc[-1]}`!'
                del doc[-1]  # Remove blank line before heading text.
            else:
                doc.append(doc_line)
        else:
            assert doc, f'Did not find any documentation before end-of-file reached!'
        assert doc, f'No documentation found before `{end}` reached!'
        if not doc[0].strip():
            del doc[0]  # Some doc comments have a leading blank line!
        self.typeshed.append(f'''
{in_str}{return_plus_in_str.join(new.rstrip().splitlines())}:
{in_str}   """
{in_str}{return_plus_in_str.join(doc).rstrip()}
{in_str}   """
''')

    def extra_notes(self, *, end: str, first_line: str = '   \n'):
        doc = [first_line]
        for doc_line in self.lines:
            if doc_line.lstrip().startswith(end):
                self.lines.push_line(doc_line)
                break
            doc.append(f'   {doc_line}\n')
        else:
            assert doc, f'Did not find before last line reached: `{end}`'
        self.typeshed[self._last_class_index] = \
            self.typeshed[self._last_class_index][:self._last_line_index] + \
            ''.join(doc).rstrip() + \
            '\n' + \
            self.typeshed[self._last_class_index][self._last_line_index:]

    def constants(self) -> None:
        typeshed_modified = False
        for line in self.lines:
            if not line.strip():  # Ignore blank lines.
                continue
            if not line.startswith('.. data:: '):
                self.lines.push_line(line)
                assert typeshed_modified, 'No constants found!'
                return
            names = []
            self.lines.push_line(line)  # Push back the current line so that it is re-read into `name_line`.
            for name_line in self.lines:
                last_dot = name_line.rfind('.')
                if last_dot < 0:
                    break  # End of name list (all the names contain a dot).
                names.append(name_line[last_dot + 1:])
            else:
                assert names, 'No constant names found!'
            description = next(self.lines)
            declarations = []
            for const_name in names:
                declarations.append(f'''
   {const_name}: int = ...
   """
{description}
   """
'''
                                    )
            self.typeshed.insert(
                self._last_class_index + 1,
                '\n'.join(declarations) + '\n\n'
            )
            typeshed_modified = True

    def defs(self, *, class_: str, old2new: Dict[str, str]) -> None:
        for line in self.lines:
            if not line.strip():  # Ignore blank lines.
                continue
            if not line.startswith('.. method:: ' + class_):
                self.lines.push_line(line)
                break
            methods = []
            self.lines.push_line(line)  # Push back the current line so that it is re-read into `name_line`.
            for method_line in self.lines:
                last_dot = method_line.rfind('.')
                if last_dot < 0:
                    break  # End of name list (all the names contain a dot).
                new = old2new[method_line[last_dot + 1:]]
                if new:  # A blank translation means the method signature is not required.
                    methods.append(new)
            else:
                assert methods, 'No method signatures found!'
            description_lines = []
            for desc_line in self.lines:
                blank = not desc_line or desc_line.isspace()
                if description_lines and blank:
                    break  # End of description.
                if not blank:
                    description_lines.append(desc_line)
            else:
                assert description_lines, 'No description found!'
            description = '\n  '.join(description_lines)
            declarations = []
            for method in methods:
                declarations.append(f'''
   {method}:
      """
  {description}
      """''')
            self.typeshed.append('\n'.join(declarations))
        else:
            assert False, 'No defs found!'

    def preview(self) -> None:
        print('\n'.join(self.typeshed))

    def write(self) -> None:
        with open(self.output_dir + self.name + '.pyi', 'w') as f:
            f.write('\n'.join(self.typeshed))
        self.typeshed.clear()
