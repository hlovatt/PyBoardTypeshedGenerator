"""
Generate `pyi` from corresponding `rst` docs.
"""

import rst
from rst2pyi import RST2PyI

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = "7.5.2"  # Version set by https://github.com/hlovatt/tag2ver


def btree(shed: RST2PyI) -> None:
    module_post_doc = f"""
from typing import Any, Final, Iterable

from uio import IOBase

"""
    shed.module(
        name="btree",
        old="simple BTree database",
        post_doc=module_post_doc,
        end="Functions",
    )
    shed.pyi.doc.extend(shed.extra_notes(end="Functions"))
    shed.def_(
        old=r".. function:: open(stream, *, flags=0, pagesize=0, cachesize=0, minkeypage=0)",
        new="""
def open(
   stream: IOBase[bytes, Any], 
   /, 
   *, 
   flags: int = 0, 
   pagesize: int = 0, 
   cachesize: int = 0, 
   minkeypage: int = 0
) -> _BTree
""",
        indent=0,
    )
    close_str = ".. method:: btree.close()"
    shed.class_(
        name="_BTree", end=close_str,
    )
    shed.def_(
        old=close_str, new="def close(self) -> None",
    )
    shed.def_(
        old=".. method:: btree.flush()", new="def flush(self) -> None",
    )
    iter_str = ".. method:: btree.__iter__()"
    shed.defs_with_common_description(
        cmd=".. method:: btree.",
        old2new={
            "__getitem__(key)": "def __getitem__(self, key: bytes, /) -> bytes",
            "get(key, default=None, /)": "def get(self, key: bytes, default: bytes | None = None, /) -> bytes | None",
            "__setitem__(key, val)": "def __setitem__(self, key: bytes, val: bytes, /) -> None",
            "__delitem__(key)": "def __delitem__(self, key: bytes, /) -> None",
            "__contains__(key)": "def __contains__(self, key: bytes, /) -> bool",
        },
        end=iter_str,
    )
    shed.def_(
        old=iter_str, new="def __iter__(self) -> Iterable[bytes]",
    )
    shed.defs_with_common_description(
        cmd=".. method:: btree.",
        old2new={
            "keys([start_key, [end_key, [flags]]])": """
def keys(
   self, 
   start_key: bytes | None = None, 
   end_key: bytes | None = None, 
   flags: int = 0, 
   /
) -> Iterable[bytes]
""",
            "values([start_key, [end_key, [flags]]])": """
def values(
   self, 
   start_key: bytes | None = None, 
   end_key: bytes | None = None, 
   flags: int = 0, 
   /
) -> Iterable[bytes]
""",
            "items([start_key, [end_key, [flags]]])": """
def items(
   self, 
   start_key: bytes | None = None, 
   end_key: bytes | None = None, 
   flags: int = 0, 
   /
) -> Iterable[tuple[bytes, bytes]]
""",
        },
        end="Constants",
    )
    shed.consume_minuses_underline_line(and_preceding_lines=True)
    shed.vars(
        old=".. data:: INCL", class_var=None,
    )
    shed.vars(
        old=".. data:: DESC", class_var=None, end=None,
    )
    shed.write()
