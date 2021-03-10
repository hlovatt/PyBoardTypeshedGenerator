"""
Generate `pyi` from corresponding `rst` docs.
"""

import rst
from rst2pyi import RST2PyI

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = "3.5.0"  # Version set by https://github.com/hlovatt/tag2ver


def uarray(shed: RST2PyI) -> None:
    shed.module(
        name='uarray',
        old='efficient arrays of numeric data',
        post_doc='''
from typing import overload, Sequence, Any, MutableSequence, Generic, Text, TypeVar

_T = TypeVar("_T", int, float, Text)
''',
        end=r'|see_cpython_module| :mod:`python:array`.'
    )
    shed.class_(name='array(MutableSequence[_T], Generic[_T])', end='Classes')
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
    # Methods not present in `rst` file.
    shed.pyi.classes[-1].defs.append('''
   def decode(self, encoding: str = "utf-8", errors: str = "strict") -> str:
      """
        Deprecated *do not use*, likely to be removed in future!
        
        Note: ``decode`` is only meant to be present for ``bytearray``, 
        but for efficiency of code-size reasons ``bytearray`` is implemented with the same code as the 
        other array type-codes and hence ``decode`` is on all ``array``s at present.
      """   
   
   @overload
   def __delitem__(self, i: int) -> None:
      """``array`` object does not support item deletion."""

   @overload
   def __delitem__(self, sl: slice) -> None:
      """``array`` object does not support item deletion."""
   
   def insert(self, index: int, value: _T) -> None:
      """``array`` object does not support item insertion."""

   @overload
   def __getitem__(self, index: int) -> _T:
      """
        Indexed read of ``self``; called as ``a[index]``, where ``a`` is an ``array``.
        Returns the value at the given ``index``. 
        Negative indices count from end and ``IndexError``is thrown if the index out of range.
        **Note:** ``__getitem__`` cannot be called directly (``a.__getitem__(index)`` fails) and
        is not present in ``__dict__``, however ``a[index]`` does work.
      """
   
   @overload
   def __getitem__(self, sl: slice) -> "array"[_T]:
      """
        Slice read of ``self``; called as ``a[sl]``, where ``a`` is an ``array``.
        Returns an ``array`` of values for the given slice. 
        Negative slice indices count from end and ``IndexError``is thrown if any of the slice indices are out of range.
        **Note:** ``__getitem__`` cannot be called directly (``a.__getitem__(sl)`` fails) and
        is not present in ``__dict__``, however ``a[sl]`` does work.
      """
      
   @overload
   def __setitem__(self, index: int, value: _T) -> None:
      """
        Indexed write into ``self``; called as ``a[index] = value`` where ``a`` is an ``array``,
        ``index`` is an ``int``, and ``value`` is the same type as ``a``'s content.
        Negative indices count from end and ``IndexError``is thrown if the index out of range.
        **Note:** ``__setitem__`` cannot be called directly (``a.__setitem__(index, value)`` fails) and
        is not present in ``__dict__``, however ``a[index] = value`` does work.
      """
      
   @overload
   def __setitem__(self, sl: slice, values: "array"[_T]) -> None:
      """
        Indexed write into ``self``; called as ``a[sl] = values``, where ``a`` is an ``array``,
        ``sl`` is an ``slice``, and ``values`` is the same type as ``a``.
        Negative indices count from end and ``IndexError``is thrown if any of the slice indices are out of range.
        **Note:** ``__setitem__`` cannot be called directly (``a.__setitem__(index, value)`` fails) and
        is not present in ``__dict__``, however ``a[index] = value`` does work.
      """
      
   def __len__(self) -> int:
      """
        Returns the number of items in ``self``; called as ``len(a)``, where ``a`` is an ``array``.
        **Note:** ``__len__`` cannot be called directly (``a.__len__()`` fails) and the 
        method is not present in ``__dict__``, however ``len(a)`` does work.
      """
      
   def __add__(self, other: "array"[_T]) -> "array"[_T]:
      """
        Return a new ``array`` that is the concatenation of ``self`` with ``other``;
        called as ``a + other`` (where ``a`` and ``other`` are both ``array``s).
        **Note:** ``__add__`` cannot be called directly (``a.__add__(other)`` fails) and
        is not present in ``__dict__``, however ``a + other`` does work.
      """
      
   def __iadd__(self, other: "array"[_T]) -> None:
      """
        Concatenates ``self`` with ``other`` in-place;
        called as ``a += other``, where ``a`` and ``other`` are both ``array``s.
        Equivalent to ``extend(other)``.
        **Note:** ``__iadd__`` cannot be called directly (``a.__iadd__(other)`` fails) and
        is not present in ``__dict__``, however ``a += other`` does work.
      """
      
   def __repr__(self) -> str:
      """
        Returns the string representation of ``self``; called as ``str(a)`` or ``repr(a)```, 
        where ``a`` is an ``array``.
        Returns the string 'array(<type>, [<elements>])', 
        where ``<type>`` is the type code letter for ``self`` and ``<elements>`` is a 
        comma separated list of the elements of ``self``.
        **Note:** ``__repr__`` cannot be called directly (``a.__repr__()`` fails) and
        is not present in ``__dict__``, however ``str(a)`` and ``repr(a)`` both work.
      """
'''.rstrip())
    shed.write()
