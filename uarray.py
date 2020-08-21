import rst
from rst2pyi import RST2PyI

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = rst.__version__


def uarray(shed: RST2PyI):
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
