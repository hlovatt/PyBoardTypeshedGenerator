from dataclasses import dataclass, field
from typing import List, Set, Dict, Callable, Optional, Union, ClassVar

from rst import RST
import rst

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = rst.__version__


@dataclass
class RST2PyI:
    """
    Converts `.rst` documentation files into `.pyi` typeshed stub interfaces.
    The conversion process is declarative and after declaring the module follows whatever order the `.rst` file is in:

      1. Create a `RST2PyI`.
      2. Declare the `module`.
      3. Declare the `def_`s in the module (functions).
      4. Declare the `class_from_file`s and/or `class_`s in the module.
      5. Declare the `def_`s inside the classes (methods and static methods).
      6. `.rst` files might at any point contain `extra_notes`, `vars`, and `defs_with_common_description`.
      7. `preview` the conversions so far (useful for debugging).
      8. `write` the finished conversion to the `.pyi` file (the point of the exercise!).
      9. Repeat 2 to 8 for each module.

    A simple example of using `RST2PyI` is `uarray.py` and a complicated example is `pyb.py`.
    """

    output_dir: str
    name: Optional[str] = None
    input_base_url: str = r'https://raw.githubusercontent.com/micropython/micropython/master/docs/library/'
    pyi: List[str] = field(default_factory=list)
    rst: RST = RST()
    last_class_index: int = 0
    last_line_index: int = 0

    _title_underline: ClassVar[Set[str]] = set('=')
    _header_underline: ClassVar[Set[str]] = set('-')
    _synopsis: ClassVar[str] = '   :synopsis: '
    _definitions: ClassVar[str] = '.. '
    _note: ClassVar[str] = '.. note::'

    def is_last(self, line: str, end: Optional[str]) -> bool:
        """
        Many of the parsing functions have an end argument, this function is used for end testing.
        If `line` is `end` then the line is pushed-back and `True` returned, else no push-back and `False`.
        Testing for `end` is slightly more complicated than simply comparing lines:

          1. If `end` is `None` return false.
          2. White space is stripped from the start to account for indentation.
          3. If the line starts with definition `self._note` then it is not an end line
          (this is because the default end line is `self._definitions`,
          but the note definition is part of the current parsing unit - its a note!).
          4. `end` is compared to the start of `line` (to allow partial matches).

        :param line: The line to be tested.
        :param end: The line to test for (if `None` returns false).
        :return: True if `line` is `end` line.
        """
        if end is None:
            return False
        s_line = line.lstrip()
        if not s_line.startswith(self._note) and s_line.startswith(end):
            self.rst.push_line(line)
            return True
        return False

    def consume(self, *, end: str):
        for line in self.rst:
            if self.is_last(line, end):
                break

    def consume_line(self, test: Callable[[str], bool], *, msg: str, and_preceding_lines: bool = False) -> None:
        if and_preceding_lines:
            for line in self.rst:
                if test(line):
                    break
            else:
                assert False, f'Expected {msg}, but reached end-of-file before finding it!'
        else:
            line = next(self.rst)
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
        self.consume_line(lambda s: name in s, msg=name, and_preceding_lines=and_preceding_lines)

    def module(
            self,
            *,
            name: str,
            old: str,
            new: Optional[str] = None,
            post_doc: str = '',
            end: str = _definitions
    ) -> None:
        self.name = name
        url = self.input_base_url + name + '.rst'
        self.rst.push_url(url)
        for line in self.rst:
            if line.startswith(self._synopsis):
                break
        else:
            assert False, f'Expected synopsis of `{old}`, but did not find it!'
        if new is None:
            new = old
        self.pyi.append(f'''"""
{new}

Descriptions taken from 
`{url}`, etc.
"""

__author__ = "{rst.__author__}"
__copyright__ = "{rst.__copyright__}"
__license__ = "{rst.__license__}"
__version__ = "{rst.__version__}"


{post_doc}
'''
                        )
        for line in self.rst:
            if self.is_last(line, end):  # Skip over lines to end of synopsis.
                break

    def class_from_file(
            self,
            *,
            old: str,
            super_class: Optional[str] = None,
            post_doc: str = '',
            end: Optional[str] = None,
    ) -> None:
        self.last_class_index = len(self.pyi)
        self.last_line_index = -(len(post_doc) + 7)
        for line in self.rst:
            if line.lstrip().startswith(old):
                url = self.input_base_url + old.strip()
                self.rst.push_url(url)
                break
        else:
            assert False, f'Did not find: `{old}`!'
        rst_file_name = old[old.find('.') + 1:]
        class_name = rst_file_name[:rst_file_name.find('.')]
        if super_class is not None:
            class_name = f'{class_name}({super_class})'
        for class_title_lines in self.rst:  # Consume class title lines.
            if class_title_lines and set(class_title_lines).issubset(self._title_underline):
                break
        self.consume_blank_line()
        doc = []
        for doc_line in self.rst:
            if self.is_last(doc_line, end):
                break
            if doc_line and set(doc_line).issubset(self._header_underline):
                assert doc[-1].strip(), f'Expected a non-blank line, got blank!'  # Remove header.
                del doc[-1]
                assert not doc[-1].strip(), f'Expected a blank line, got `{doc[-1]}`!'
                del doc[-1]
                break
            doc.append(f'   {doc_line}\n')
        else:
            assert doc, 'Did not find any class documentation.'
        self.pyi.append(f'''
class {class_name}: 
   """
{''.join(doc).rstrip()}
   """{post_doc}
'''
                        )

    def class_(self, *, name: str, end: str) -> None:
        self.pyi.append(f'''
class {name}:
   """
   """
''')
        self.last_class_index = len(self.pyi) - 1
        self.last_line_index = -7
        self.extra_notes(end=end, first_line='')

    def defs_with_common_description(
            self,
            *,
            cmd: str,
            old2new: Dict[str, Union[str, List[str]]],
            end: Optional[str] = None,
            indent: int = 3
    ) -> None:
        for line in self.rst:
            if self.is_last(line, end):
                break
            if not line.strip():  # Ignore blank lines.
                continue
            if not line.startswith(cmd):
                self.rst.push_line(line)
                break
            new_defs = []
            self.rst.push_line(line)  # Push back the current line so that it is re-read into `def_line`.
            for def_line in self.rst:
                if not def_line:
                    break  # End of name list.
                new = old2new[def_line[len(cmd):]]
                if new:  # A blank translation or an empty list means the method signature(s) is(are) not required.
                    if isinstance(new, list):
                        for overload in new:
                            new_defs.append('@overload\n' + overload)
                    else:
                        new_defs.append(new)
            else:
                assert new_defs, 'No method signatures found!'
            doc = []
            for doc_line in self.rst:
                if self.is_last(doc_line, end):
                    break
                doc.append(doc_line)
            else:
                assert doc, 'No description found!'
            for new in new_defs:
                self._add_def_or_defs(doc, indent, new)
        else:
            assert False, 'No defs found!'

    def def_(
            self,
            *,
            old: str,
            new: Union[str, List[str]],
            extra_docs: List[str] = [],
            indent: int = 3,
            end: str = _definitions
    ) -> None:
        old = old.strip()
        self.consume_name_line(old, and_preceding_lines=True)
        self.consume_line(
            lambda s: not s.strip() or s.startswith('   :noindex:'),
            msg='a blank line or `:noindex:` line'
        )
        doc = []
        for doc_line in self.rst:
            if self.is_last(doc_line, end):
                break
            if doc_line and set(doc_line).issubset(self._header_underline):
                assert doc[-1], f'Expected heading, got blank line!'
                del doc[-1]  # Remove heading text (which is followed by detected underline).
                assert not doc[-1].strip(), f'Expected blank line, got `{doc[-1]}`!'
                del doc[-1]  # Remove blank line before heading text.
                for para_line in self.rst:  # Consume heading paragraph text (if any).
                    if self.is_last(para_line, self._definitions):
                        break
                else:
                    assert False, 'Reached end of file whilst stepping over heading paragraph text!'
            else:
                doc.append(doc_line)
        else:
            assert doc, f'No documentation found before end-of-file reached!'
        assert doc, f'No documentation found before `{end}` reached!'
        if extra_docs:
            doc.extend(extra_docs)
        self._add_def_or_defs(doc, indent, new)

    def _add_def_or_defs(self, doc: List[str], indent: int, new: Union[List[str], str]):
        if not doc[0].strip():
            del doc[0]  # Some doc comments have a leading blank line!
        in_str, return_plus_in_str = RST2PyI._indent_strings(indent)
        doc_str = RST2PyI._doc_str_gen(doc, in_str, return_plus_in_str)
        if isinstance(new, str):
            self._add_def(new, doc_str, in_str, return_plus_in_str)
        else:
            for new_def in new:
                self._add_def('@overload\n' + new_def.lstrip(), doc_str, in_str, return_plus_in_str)

    @staticmethod
    def _indent_strings(indent: int):
        in_str = indent * ' '
        return_plus_in_str = '\n' + in_str
        return in_str, return_plus_in_str

    @staticmethod
    def _doc_str_gen(doc: List[str], in_str: str, return_plus_in_str: str):
        return f'''
{in_str}   """
{in_str}{return_plus_in_str.join(doc).rstrip()}
{in_str}   """
'''

    def _add_def(self, new: str, doc_str: str, in_str: str, return_plus_in_str: str) -> None:
        self.pyi.append(f'{in_str}{return_plus_in_str.join(new.rstrip().splitlines())}:{doc_str}')

    def extra_docs(self, *, indent: int = 3, end: str = _definitions) -> List[str]:
        doc = []
        indent_str = indent * ' '
        for doc_line in self.rst:
            if self.is_last(doc_line, end):
                break
            doc.append(indent_str + doc_line)
        else:
            assert doc, 'No extra documentation found before end-of-file reached!'
        assert doc, f'No extra documentation before `{end}` reached!'
        return doc

    def extra_notes(self, *, end: str, first_line: str = '   \n'):
        doc = [first_line]
        for doc_line in self.rst:
            if self.is_last(doc_line, end):
                break
            doc.append(f'   {doc_line}\n')
        else:
            assert doc, 'No extra notes found before end-of-file reached!'
        assert doc, f'No extra notes found before `{end}` reached!'
        self.pyi[self.last_class_index] = \
            self.pyi[self.last_class_index][:self.last_line_index] + \
            ''.join(doc).rstrip() + \
            '\n' + \
            self.pyi[self.last_class_index][self.last_line_index:]

    def vars(
            self,
            *,
            type_: str = 'int',
            class_var: Optional[bool] = True,
            end: Optional[str] = _definitions
    ) -> None:
        """
        Add var definitions to current typeshed.
        Class-vars (`class_var=True`) and instance-vars (`class_var=False`)
        are added to the typeshed at `self.last_class_index + 1`,
        i.e. inside the class definition immediately after the doc comment.
        Module vars (`class_var=None`) are added at `self.last_class_index`,
        i.e. immediately before the class definition.
        If there is no class definition yet, i.e. `self.last_class_index` is 0,
        then the vars are added to the end of `self.pyi`.
        `self.last_class_index` is typically set by `self.class_` or `self.class_from_file`.
        if `class_var=None` and `self.last_class_index` is not 0
        then `self.last_class_index` is incremented by this method,
        so that `self.last_class_index` still points to the class.
        However subsequent calls to this method with `class_var` either true or false (not module var)
        insert the declarations immediately below the class declaration,
        i.e. in reverse order!

        :param type_: the type of the var as a string (defaults to `int`)
        :param class_var: true (default) if class variables are to be added,
        false for instance, and `None` for file-scope variables.
        :param end: the end of field parsing string prefix (defaults to `self._definitions`) and
        `None` means parse to end of file.
        :return: `None`
        """
        type_hint = f'ClassVar[{type_}]' if class_var else type_
        typeshed_modified = False
        for line in self.rst:
            if self.is_last(line, end):
                assert typeshed_modified, 'No constants found!'
                break
            if not line.strip():  # Ignore blank lines.
                continue
            if not line.startswith('.. data:: '):
                self.rst.push_line(line)
                assert typeshed_modified, 'No constants found!'
                return
            names = []
            self.rst.push_line(line)  # Push back the current line so that it is re-read into `name_line`.
            for name_line in self.rst:
                last_dot = name_line.rfind('.')
                if last_dot < 0:
                    break  # End of name list (all the names contain a dot).
                names.append(name_line[last_dot + 1:])
            else:
                assert names, 'No constant names found!'
            description_lines = []
            for desc_line in self.rst:
                if self.is_last(desc_line, self._definitions) or self.is_last(desc_line, end):
                    break
                description_lines.append(desc_line)
            else:
                assert description_lines, 'No description found!'
            while not description_lines[0]:
                del description_lines[0]  # Remove leading blank lines.
            description = "\n".join(description_lines).rstrip()
            indent_str = '' if class_var is None else '   '
            declarations = []
            for const_name in names:
                declarations.append(f'''
{indent_str}{const_name}: {type_hint} = ...
{indent_str}"""
{description}
{indent_str}"""
'''
                                    )
            dec_str = '\n'.join(declarations) + '\n\n'
            if class_var is None and self.last_class_index == 0:  # Module level no classes yet.
                self.pyi.append(dec_str)
            else:
                typeshed_pos = self.last_class_index if class_var is None else self.last_class_index + 1
                self.pyi.insert(typeshed_pos, dec_str)
            if class_var is None and self.last_class_index != 0:
                self.last_class_index += 1
            typeshed_modified = True

    def preview(self) -> None:
        print('\n'.join(self.pyi))

    def write(self) -> None:
        """
        Write the module to the destination directory and reset `self` for next module.

        :return: `None`
        """
        assert not self.rst, f'Not all input lines processed! Remaining: {self.rst}'
        with open(self.output_dir + self.name + '.pyi', 'w') as f:
            f.write('\n'.join(self.pyi))
        self.name = None
        self.pyi.clear()
        self.last_line_index = 0
        self.last_class_index = 0
