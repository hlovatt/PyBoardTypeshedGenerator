"""
Minimal concept of a class, just enough to model the classes as described in the MicroPython RST docs.

Note:

  1. Does not have a concept of an inner class, because the RST docs don't describe any.
  2. The inner classes in `pyb.Pin`, `board` and `cpu`, are not documented in the RST files and are added
    'manually' by appending text to field `defs`.
"""

from dataclasses import dataclass, field
from typing import List, Optional

import rst

__author__ = rst.__author__
__copyright_ = rst.__copyright__
__license__ = rst.__license__
__version__ = "3.4.0"  # Version set by https://github.com/hlovatt/tag2ver


@dataclass
class Class:
    class_def: Optional[str] = None
    doc: List[str] = field(default_factory=list)
    imports_vars: List[str] = field(default_factory=list)
    defs: List[str] = field(default_factory=list)

    def __str__(self) -> str:
        assert self.class_def, f'No class definition string! {self.class_def}'
        new_line = '\n'  # Can't have `\` inside `{}` in an f-string!
        return f'''
{self.class_def}
   """
{new_line.join(self.doc)}
   """

{new_line.join(self.imports_vars)}

{new_line.join(self.defs)}
'''.lstrip(new_line)
