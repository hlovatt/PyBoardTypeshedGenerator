import lines
from typeshed import Typeshed

__author__ = lines.__author__
__copyright__ = lines.__copyright__
__license__ = lines.__license__
__version__ = lines.__version__


def uarray(shed: Typeshed):
    shed.module(
        name='uarray',
        old='efficient arrays of numeric data',
        post_doc='''
from typing import overload, Sequence, Any
''',
        end=r'|see_cpython_module| :mod:`python:array`.'
    )
    shed.class_(name='array', end='Classes')
    shed.def_(
        old=r'.. class:: array(typecode, [iterable])',
        new=[
            'def __init__(self, typecode: str, /)',
            'def __init__(self, typecode: str, iterable: Sequence[Any], /)'
        ],
    )
    shed.def_(
        old=r'    .. method:: append(val)',
        new='def append(self, val: Any, /) -> None',
    )
    shed.def_(
        old=r'    .. method:: extend(iterable)',
        new='def extend(self, iterable: Sequence[Any], /) -> None',
    )
    shed.write()
