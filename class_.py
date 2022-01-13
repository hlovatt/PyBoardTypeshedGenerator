"""
Minimal concept of a class, just enough to model the classes as described in the MicroPython RST docs.

Note:

  1. Does not have a concept of an inner class, because the RST docs don't describe any.
  2. The inner classes in `pyb.Pin`, `board` and `cpu`, are not documented in the RST files and are added
    'manually' by appending text to field `defs`.
"""

from dataclasses import dataclass, field
from typing import List

import rst

__author__ = rst.__author__
__copyright_ = rst.__copyright__
__license__ = rst.__license__
__version__ = "7.5.0"  # Version set by https://github.com/hlovatt/tag2ver


def strip_leading_and_trailing_blank_lines(lines: List[str]) -> List[str]:
    start = 0
    for line in lines:
        if line.strip():
            break
        start += 1
    end = len(lines)
    for line in reversed(lines):
        if line.strip():
            break
        end -= 1
    return lines[start:end]


@dataclass
class Class:
    pre_str: str = ""
    class_def: str = ""
    doc: List[str] = field(default_factory=list)
    imports_vars: List[str] = field(default_factory=list)
    defs: List[str] = field(default_factory=list)

    def __str__(self) -> str:
        assert self.class_def, f"No class definition string! {self.class_def}"
        if self.pre_str and not self.pre_str.endswith("\n"):
            self.pre_str += (
                "\n"  # Terminate with a return non-empty, non-terminated pre strings.
            )
        new_line = "\n"  # Can't have `\` inside `{}` in an f-string!
        return f'''
{(self.pre_str + self.class_def).strip()}
   """
{new_line.join(strip_leading_and_trailing_blank_lines(self.doc)).strip(new_line)}
   """

{new_line.join(strip_leading_and_trailing_blank_lines(self.imports_vars)).strip(new_line)}

{new_line.join(strip_leading_and_trailing_blank_lines(self.defs))}
'''.lstrip(
            new_line
        )
