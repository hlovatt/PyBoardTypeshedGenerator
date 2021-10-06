"""
Generate `pyi` from corresponding `rst` docs.
"""

import repdefs
import rst
from rst2pyi import RST2PyI

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = "6.2.0"  # Version set by https://github.com/hlovatt/tag2ver


def uctypes(shed: RST2PyI) -> None:
    shed.module(
        name='uctypes',
        old='access binary data in a structured way',
        post_doc=f'''
from typing import Tuple, TypeVar, Final

from uarray import array

{repdefs.ANY_READABLE_BUF}
''',
        end=R'Module contents'
    )
    rst_name = R'.. class:: struct(addr, descriptor, layout_type=NATIVE, /)'
    shed.class_(
        pre_str='# noinspection PyPep8Naming',
        name='struct',
        end=rst_name,
    )
    shed.pyi.imports_vars_defs.extend([
        '_ScalarProperty: Final = int',
        '_RecursiveProperty: Final = Tuple[int, "_property"]',
        '_ArrayProperty: Final = Tuple[int, int]',
        '_ArrayOfAggregateProperty: Final = Tuple[int, int, "_property"]',
        '_PointerToAPrimitiveProperty: Final = Tuple[int, int]',
        '_PointerToAaAggregateProperty: Final = Tuple[int, "_property"]',
        '_BitfieldProperty: Final = int',
        ('_property: Final = _ScalarProperty'
         ' | _RecursiveProperty'
         ' | _ArrayProperty'
         ' | _ArrayOfAggregateProperty'
         ' | _PointerToAPrimitiveProperty'
         ' | _PointerToAaAggregateProperty'
         ' | _BitfieldProperty'
         ),
        '_descriptor: Final = Tuple[str, _property]',
    ])
    shed.def_(
        old=rst_name,
        new='def __init__(self, addr: int, descriptor: _descriptor, layout_type: int = NATIVE, /)',
    )
    shed.vars(old='.. data:: LITTLE_ENDIAN', class_var=None)
    shed.vars(old='.. data:: BIG_ENDIAN', class_var=None)
    shed.vars(old='.. data:: NATIVE', class_var=None)
    shed.def_(
        pre_str='# noinspection PyShadowingNames',
        old=r'.. function:: sizeof(struct, layout_type=NATIVE, /)',
        new='def sizeof(struct: struct | _descriptor, layout_type: int = NATIVE, /) -> int',
        indent=0,
    )
    shed.def_(
        old=r'.. function:: addressof(obj)',
        new='def addressof(obj: _AnyReadableBuf, /) -> int',
        indent=0,
    )
    shed.def_(
        old=r'.. function:: bytes_at(addr, size)',
        new='def bytes_at(addr: int, size: int, /) -> bytes',
        indent=0,
    )
    shed.def_(
        old=r'.. function:: bytearray_at(addr, size)',
        new='def bytearray_at(addr: int, size: int, /) -> bytearray',
        indent=0,
    )
    shed.vars(
        old=[
            '.. data:: UINT8',
            'INT8',
            'UINT16',
            'INT16',
            'UINT32',
            'INT32',
            'UINT64',
            'INT64',
        ],
        class_var=None
    )
    shed.vars(
        old=[
            '.. data:: FLOAT32',
            'FLOAT64',
        ],
        class_var=None
    )
    shed.vars(old='.. data:: VOID', class_var=None)
    shed.vars(
        old=[
            '.. data:: PTR',
            'ARRAY',
        ],
        class_var=None,
        end='Structure descriptors and instantiating structure objects'
    )
    shed.extra_docs(end=None)
    shed.write()
