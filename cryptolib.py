"""
Generate `pyi` from corresponding `rst` docs.
"""

import repdefs
import rst
from rst2pyi import RST2PyI

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = "5.0.3"  # Version set by https://github.com/hlovatt/tag2ver


def cryptolib(shed: RST2PyI) -> None:
    shed.module(
        name='cryptolib',
        old='cryptographic ciphers',
        post_doc=f'''
from typing import overload, TypeVar

from uarray import array

{repdefs.AnyReadableBuf}
{repdefs.AnyWritableBuf}
''',
        end=R'Classes'
    )
    shed.consume(end='.. class:: aes')
    rst_name = R'.. classmethod:: __init__(key, mode, [IV])'
    shed.class_(
        pre_str='# noinspection PyPep8Naming',
        name='aes',
        end=rst_name,
    )
    shed.def_(
        old=rst_name,
        new=[
            'def __init__(self, key: _AnyReadableBuf, mode: int, /)',
            'def __init__(self, key: _AnyReadableBuf, mode: int, IV: _AnyReadableBuf, /)'
        ],
    )
    shed.def_(
        old='.. method:: encrypt(in_buf, [out_buf])',
        new=[
            'def encrypt(self, in_buf: _AnyReadableBuf, /) -> bytes',
            'def encrypt(self, in_buf: _AnyReadableBuf, out_buf: _AnyWritableBuf, /) -> None'
        ],
    )
    shed.def_(
        old='.. method:: decrypt(in_buf, [out_buf])',
        new=[
            'def decrypt(self, in_buf: _AnyReadableBuf, /) -> bytes',
            'def decrypt(self, in_buf: _AnyReadableBuf, out_buf: _AnyWritableBuf, /) -> None'
        ],
    )
    shed.write()
