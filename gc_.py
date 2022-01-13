"""
Generate `pyi` from corresponding `rst` docs.
"""

import rst
from rst2pyi import RST2PyI

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = "7.5.2"  # Version set by https://github.com/hlovatt/tag2ver


def gc(shed: RST2PyI) -> None:
    shed.module(
        name="gc",
        old="control the garbage collector",
        post_doc="from typing import overload",
        end="Functions",
    )
    shed.def_(
        old=".. function:: enable()", new="def enable() -> None", indent=0,
    )
    shed.def_(
        old=".. function:: disable()", new="def disable() -> None", indent=0,
    )
    shed.def_(
        old=".. function:: collect()", new="def collect() -> None", indent=0,
    )
    shed.def_(
        old=".. function:: mem_alloc()", new="def mem_alloc() -> int", indent=0,
    )
    shed.def_(
        old=".. function:: mem_free()", new="def mem_free() -> int", indent=0,
    )
    shed.def_(
        old=".. function:: threshold([amount])",
        new=["def threshold() -> int", "def threshold(amount: int) -> None"],
        indent=0,
    )
    shed.write()
