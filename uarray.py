from typeshed import Typeshed

__author__      = "Howard C Lovatt"
__copyright__   = "Howard C Lovatt, 2020 onwards."
__license__     = "MIT https://opensource.org/licenses/MIT (as used by MicroPython)."
__version__     = "0.0.0"


def uarray():
    shed = Typeshed(name='uarray')
    shed.synopsis(
        old='efficient arrays of numeric data',
        post_doc='''
from typing import overload, Sequence, Any


class array:
   """
   """
''',
        end='|see_cpython_module| :mod:`python:array`.'
    )
    shed._last_class_index = len(shed.typeshed) - 1
    shed._last_line_index = -8
    shed.extra_notes(end='Classes', first_line='')
    shed.def_(
        old=r'.. class:: array(typecode, [iterable])',
        new='''
@overload
def __init__(self, typecode: str, /): ...
@overload
def __init__(self, typecode: str, iterable: Sequence[Any], /)
''',
        indent=3,
    )
    shed.def_(
        old=r'    .. method:: append(val)',
        new='def append(self, val: Any, /) -> None',
        indent=3,
    )
    shed.def_(
        old=r'    .. method:: extend(iterable)',
        new='def extend(self, iterable: Sequence[Any], /) -> None',
        indent=3,
    )
    shed.write()
