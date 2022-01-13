"""
Generate `pyi` from corresponding `rst` docs.
"""

import rst
from rst2pyi import RST2PyI

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = "7.5.0"  # Version set by https://github.com/hlovatt/tag2ver


def cryptolib(shed: RST2PyI) -> None:
    shed.module(
        name="cryptolib",
        old="cryptographic ciphers",
        post_doc=f"""
from typing import overload

from uio import AnyReadableBuf, AnyWritableBuf
""",
        end=r"Classes",
    )
    shed.consume_up_to_but_excl_end_line(end=".. class:: aes")
    rst_name = r".. classmethod:: __init__(key, mode, [IV])"
    shed.class_(
        pre_str="# noinspection PyPep8Naming", name="aes", end=rst_name,
    )
    shed.def_(
        old=rst_name,
        new=[
            "def __init__(self, key: AnyReadableBuf, mode: int, /)",
            "def __init__(self, key: AnyReadableBuf, mode: int, IV: AnyReadableBuf, /)",
        ],
    )
    shed.def_(
        old=".. method:: encrypt(in_buf, [out_buf])",
        new=[
            "def encrypt(self, in_buf: AnyReadableBuf, /) -> bytes",
            "def encrypt(self, in_buf: AnyReadableBuf, out_buf: AnyWritableBuf, /) -> None",
        ],
    )
    shed.def_(
        old=".. method:: decrypt(in_buf, [out_buf])",
        new=[
            "def decrypt(self, in_buf: AnyReadableBuf, /) -> bytes",
            "def decrypt(self, in_buf: AnyReadableBuf, out_buf: AnyWritableBuf, /) -> None",
        ],
    )
    shed.write(u_also=True)
