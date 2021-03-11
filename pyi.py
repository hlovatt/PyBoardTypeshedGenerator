"""
Minimal concept of a typeshed file (module), just enough to model the modules as described in the MicroPython RST docs.
"""

from dataclasses import dataclass, field
from typing import List

import rst
from class_ import Class

__author__ = rst.__author__
__copyright_ = rst.__copyright__
__license__ = rst.__license__
__version__ = "3.6.0"  # Version set by https://github.com/hlovatt/tag2ver


@dataclass
class PYI:
    doc: List[str] = field(default_factory=list)
    imports_vars_defs: List[str] = field(default_factory=list)
    classes: List[Class] = field(default_factory=list)

    def __str__(self) -> str:
        new_line = '\n'  # Can't have `\` inside `{}` in an f-string!
        return f'''
"""
{new_line.join(self.doc)}
"""

{new_line.join(self.imports_vars_defs)}

{new_line.join((str(class_) for class_ in self.classes))}
'''.lstrip(new_line)

    def clear(self):
        self.doc.clear()
        self.imports_vars_defs.clear()
        self.classes.clear()
