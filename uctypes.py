"""
Generate `pyi` from corresponding `rst` docs.
"""

import repdefs
import rst
from rst2pyi import RST2PyI

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = "3.7.1"  # Version set by https://github.com/hlovatt/tag2ver


def uctypes(shed: RST2PyI) -> None:
    shed.module(
        name='uctypes',
        old='access binary data in a structured way',
        post_doc=f'''
from typing import Tuple, Union, TypeVar

from uarray import array

{repdefs.AnyReadableBuf}
''',
        end=r'Module contents'
    )
    rst_name = r'.. class:: struct(addr, descriptor, layout_type=NATIVE, /)'
    shed.class_(
        name='struct',
        end=rst_name,
    )
    shed.pyi.imports_vars_defs += [
        '_scalar_property = int',
        '_recursive_property = Tuple[int, "_property"]',
        '_array_property = Tuple[int, int]',
        '_array_of_aggregate_property = Tuple[int, int, "_property"]',
        '_pointer_to_a_primitive_property = Tuple[int, int]',
        '_pointer_to_an_aggregate_property = Tuple[int, "_property"]',
        '_bitfield_property = int',
        ('_property = Union['
            '_scalar_property, '
            '_recursive_property, '
            '_array_property, '
            '_array_of_aggregate_property, '
            '_pointer_to_a_primitive_property, '
            '_pointer_to_an_aggregate_property, '
            '_bitfield_property'
        ']'),
        '_descriptor = Tuple[str, _property]',
    ]
    shed.def_(
        old=rst_name,
        new='def __init__(self, addr: int, descriptor: _descriptor, layout_type: int = NATIVE, /)',
    )
    shed.vars(class_var=None)
    shed.vars(class_var=None)
    shed.vars(class_var=None)
    shed.def_(
        pre_str='# noinspection PyShadowingNames',
        old=r'.. function:: sizeof(struct, layout_type=NATIVE, /)',
        new='def sizeof(struct: Union["struct", _descriptor], layout_type: int = NATIVE, /) -> int',
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
    shed.vars(class_var=None)
    shed.vars(class_var=None)
    shed.vars(class_var=None)
    shed.vars(class_var=None, end='Structure descriptors and instantiating structure objects')
    shed.extra_docs(end=None)
    shed.write()
