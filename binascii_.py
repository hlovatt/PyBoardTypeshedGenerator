"""
Generate `pyi` from corresponding `rst` docs.
"""

import rst
from rst2pyi import RST2PyI

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = "7.3.0"  # Version set by https://github.com/hlovatt/tag2ver


def binascii(shed: RST2PyI) -> None:
    shed.module(name="binascii", old="binary/ASCII conversions", end=r"Functions")
    shed.def_(
        old=r".. function:: hexlify(data, [sep])",
        new="def hexlify(data: bytes, sep: str | bytes = ..., /) -> bytes",
        indent=0,
    )
    shed.def_(
        old=r".. function:: unhexlify(data)",
        new="def unhexlify(data: str | bytes, /) -> bytes",
        indent=0,
    )
    shed.def_(
        old=r".. function:: a2b_base64(data)",
        new="def a2b_base64(data: str | bytes, /) -> bytes",
        indent=0,
    )
    shed.def_(
        old=r".. function:: b2a_base64(data)",
        new="def b2a_base64(data: bytes, /) -> bytes",
        indent=0,
    )
    shed.write(u_also=True)
