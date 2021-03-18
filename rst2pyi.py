"""
Routines to converts `.rst` documentation files into `.pyi` typeshed stub interfaces.
"""

from dataclasses import dataclass
from typing import List, Set, Dict, Callable, Optional, Union, ClassVar, Final

import rst
from class_ import Class
from pyi import PYI
from rst import RST

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = "3.7.2"  # Version set by https://github.com/hlovatt/tag2ver


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
      6. `.rst` files might at any point contain `extra_notes`, `imports_vars`, and `defs_with_common_description`.
      7. `preview` the conversions so far (useful for debugging).
      8. `write` the finished conversion to the `.pyi` file (the point of the exercise!).
      9. Repeat 2 to 8 for each module.

    A simple example of using `RST2PyI` is `uarray.py` and a complicated example is `pyb.py`.
    """

    output_dir: str
    _name: Optional[str] = None
    _input_base_url: Final[str] = r'https://raw.githubusercontent.com/micropython/micropython/master/docs/library/'
    pyi: PYI = PYI()
    rst: RST = RST()

    _title_underline: ClassVar[Set[str]] = set('=')
    _header_underline: ClassVar[Set[str]] = set('-')
    _synopsis: ClassVar[str] = '   :synopsis: '
    _definitions: ClassVar[str] = '.. '
    _note: ClassVar[str] = '.. note::'
    _data_dec_str: ClassVar[str] = ' data:: '

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

    def consume(self, *, end: str) -> None:
        self.consume_line(lambda l: self.is_last(l, end), msg=end, and_preceding_lines=True)

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

    def consume_synopsis_line(self, name: str, *, and_preceding_lines: bool = False) -> None:
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
        self._name = name
        url = self._input_base_url + name + '.rst'
        self.rst.push_url(url)
        self.consume_synopsis_line(name=old, and_preceding_lines=True)
        if new is None:
            new = old
        doc = []
        for doc_line in self.rst:
            if self.is_last(doc_line, end):
                break
            doc.append(doc_line)
        new_line = '\n'  # Needed because you can't have a `\` inside a `{}` block in an f-string.
        self.pyi.doc.append(f'''
{new}

Descriptions taken from 
`{url}`, etc.

{new_line.join(doc).strip()}
'''
                            )
        self.pyi.imports_vars_defs.append(f'''

__author__ = "{rst.__author__}"
__copyright__ = "{rst.__copyright__}"
__license__ = "{rst.__license__}"
__version__ = "3.7.2"  # Version set by https://github.com/hlovatt/tag2ver


{post_doc}
'''
                                          )

    def class_from_file(
            self,
            *,
            pre_str: str = '',
            old: str,
            super_class: Optional[str] = None,
            post_doc: str = '',
            end: Optional[str] = None,
    ) -> None:
        for line in self.rst:
            if line.lstrip().startswith(old):
                url = self._input_base_url + old.strip()
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
            doc.append(f'   {doc_line}')
        else:
            assert doc, 'Did not find any class documentation.'
        new_class = Class(pre_str=pre_str)
        self.pyi.classes.append(new_class)
        new_class.class_def = f'class {class_name}:'
        new_class.doc = doc
        new_class.imports_vars.append(post_doc)

    def class_(self, *, pre_str: str = '', name: str, end: str) -> None:
        new_class = Class(pre_str=pre_str)
        self.pyi.classes.append(new_class)
        new_class.class_def = f'class {name}:'
        new_class.doc = self.extra_notes(end=end, first_line='')

    def defs_with_common_description(
            self,
            *,
            pre_str: str = '',
            cmd: str,
            old2new: Dict[str, Union[str, List[str]]],
            end: Optional[str] = None,
            indent: int = 3,
            extra_doc_indent: int = 0,
    ) -> None:
        method_def = indent != 0
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
                    break  # End of _name list.
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
                self._add_def_or_defs(method_def, doc, indent, extra_doc_indent, new, pre_str)
        else:
            assert False, 'No defs found!'

    def def_(
            self,
            *,
            pre_str: str = '',
            old: str,
            new: Union[str, List[str]],
            extra_docs: List[str] = (),
            indent: int = 3,
            extra_doc_indent: int = 0,
            end: str = _definitions
    ) -> None:
        method_def = indent != 0
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
        self._add_def_or_defs(method_def, doc, indent, extra_doc_indent, new, pre_str)

    def _add_def_or_defs(
            self,
            method_def: bool,
            doc: List[str],
            indent: int,
            extra_doc_indent: int,
            new: Union[List[str], str],
            pre_str: str = '',
    ):
        if not doc[0].strip():
            del doc[0]  # Some class_def_and_doc comments have a leading blank line!
        first_line_indent = RST2PyI._indent(doc[0])  # Some lines, e.g. note lines, are not/incorrectly indented.
        for i in range(1, len(doc)):
            line_indent = RST2PyI._indent(doc[i])
            indent_diff = first_line_indent - line_indent
            if indent_diff > 0:
                doc[i] = indent_diff * ' ' + doc[i]
        in_str, doc_in_str = RST2PyI._indent_strings(indent, extra_doc_indent)
        doc_str = RST2PyI._doc_str_gen(doc, in_str, doc_in_str)
        if isinstance(new, str):
            self._add_def(method_def, new, doc_str, in_str, pre_str)
        else:
            for new_def in new:
                self._add_def(method_def, '@overload\n' + new_def.lstrip(), doc_str, in_str, pre_str)

    @staticmethod
    def _indent(s: str) -> int:
        return len(s) - len(s.lstrip())

    @staticmethod
    def _indent_strings(indent: int, extra_doc_indent: int):
        in_str = indent * ' '
        doc_in_str = in_str + extra_doc_indent * ' '
        return in_str, doc_in_str

    @staticmethod
    def _doc_str_gen(doc: List[str], in_str: str, doc_in_str: str):
        return_plus_doc_in_str = '\n' + doc_in_str
        return f'''
{in_str}   """
{doc_in_str}{return_plus_doc_in_str.join(doc).rstrip()}
{in_str}   """
'''

    def _add_def(self, method_def: bool, new: str, doc_str: str, in_str: str, pre_str: str) -> None:
        where = self.pyi.classes[-1].defs if method_def else self.pyi.imports_vars_defs
        if pre_str:
            if not pre_str.endswith('\n'):
                pre_str += '\n'  # Terminate a non-empty, non-terminated pre-string with a return.
        return_plus_in_str = '\n' + in_str
        in_str = pre_str + in_str  # Every def has the pre-string prepended.
        where.append(f'{in_str}{return_plus_in_str.join(new.rstrip().splitlines())}:{doc_str}')

    def _extras(self, *, description: str, indent: int, end: Optional[str], first_line: str) -> List[str]:
        extras = [first_line]
        indent_str = indent * ' '
        for extra_line in self.rst:
            if self.is_last(extra_line, end):
                break
            extras.append(indent_str + extra_line)
        else:
            assert extras, f'No extra {description} found before end-of-file reached!'
        assert extras, f'No extra {description} before `{end}` reached!'
        return extras

    def extra_docs(self, *, indent: int = 3, end: Optional[str] = _definitions) -> List[str]:
        return self._extras(description='documentation', indent=indent, end=end, first_line='')

    def extra_notes(self, *, end: Optional[str], first_line: str = '   \n') -> List[str]:
        return self._extras(description='notes', indent=3, end=end, first_line=first_line)

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
        are added to the top of the current class`,
        i.e. inside the class definition after the class doc-comment and import statements.
        Module-vars (`class_var=None`) are added at at the top of the file,
        i.e. after the file doc-comment.

        :param type_: the type of the var as a string (defaults to `int`)
        :param class_var: true (default) if class variables are to be added,
        false for instance, and `None` for file-scope variables.
        :param end: the end of field parsing string prefix (defaults to `self._definitions`) and
        `None` means parse to end of file.
        """
        type_hint = f'ClassVar[{type_}]' if class_var else type_
        typeshed_modified = False
        for line in self.rst:
            if not line.strip():  # Ignore blank lines.
                continue
            if (typeshed_modified or not line.startswith('.. data:: ')) and self.is_last(line, end):
                assert typeshed_modified, 'No constants found!'
                break
            names = []
            last_dot = line.rfind('.')
            name_indent = ' ' * max(len(RST2PyI._data_dec_str) + 2, last_dot)
            self.rst.push_line(line)  # Push back the current line so that it is re-read into `name_line`.
            for name_line in self.rst:
                if name_line.startswith(name_indent):
                    name = name_line[len(name_indent):]
                else:
                    last_dot = name_line.rfind('.')
                    if last_dot < 0:
                        break  # End of vars listed in file (all the names contain a dot or are indented as first name).
                    temp_name = name_line[last_dot + 1:]
                    name = temp_name \
                        if last_dot >= 0 and not temp_name.startswith(RST2PyI._data_dec_str) \
                        else temp_name[len(RST2PyI._data_dec_str):]
                names.append(name.rstrip())
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
            for var_name in names:
                declarations.append(f'''
{indent_str}{var_name}: {type_hint} = ...
{indent_str}"""
{description}
{indent_str}"""
'''
                                    )
            dec_str = '\n'.join(declarations) + '\n\n'
            if class_var is None:  # Module level.
                self.pyi.imports_vars_defs.append(dec_str)
            else:
                self.pyi.classes[-1].imports_vars.append(dec_str)
            typeshed_modified = True

    def preview(self) -> None:
        print(self.pyi)

    def write(self) -> None:
        """
        Write the module to the destination directory and reset `self` for next module.

        :return: `None`
        """
        assert not self.rst, f'Not all input lines processed! Remaining: {self.rst}'
        with open(self.output_dir + self._name + '.pyi', 'w') as f:
            f.write(str(self.pyi))
        self._name = None
        self.pyi.clear()
