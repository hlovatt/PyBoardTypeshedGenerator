"""
Generate `pyi` from corresponding `rst` docs.
"""

import rst
from rst2pyi import RST2PyI

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = "7.3.0"  # Version set by https://github.com/hlovatt/tag2ver


def struct(shed: RST2PyI) -> None:
    shed.module(
        name="struct",
        old="pack and unpack primitive data types",
        post_doc="""
from typing import Any

from uio import AnyReadableBuf, AnyWritableBuf
""",
        end="Functions",
    )

    shed.def_(
        old=r".. function:: calcsize(fmt)",
        new="def calcsize(fmt: str | bytes, /,) -> int",
        indent=0,
    )
    shed.def_(
        old=r".. function:: pack(fmt, v1, v2, ...)",
        new="def pack(fmt: str | bytes, /, *v: Any) -> bytes",
        indent=0,
    )
    shed.def_(
        old=r".. function:: pack_into(fmt, buffer, offset, v1, v2, ...)",
        new="def pack_into(fmt: str | bytes, buffer: AnyWritableBuf, offset: int, /, *v: Any) -> None",
        indent=0,
    )
    shed.def_(
        old=r".. function:: unpack(fmt, data)",
        new="def unpack(fmt: str | bytes, data: AnyReadableBuf, /) -> tuple[Any, ...]",
        indent=0,
    )
    shed.def_(
        old=r".. function:: unpack_from(fmt, data, offset=0, /)",
        new="def unpack_from(fmt: str | bytes, data: AnyReadableBuf, offset: int = 0, /) -> tuple[Any, ...]",
        indent=0,
    )

    shed.write(u_also=True)
