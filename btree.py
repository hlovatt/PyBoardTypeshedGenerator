"""
Generate `pyi` from corresponding `rst` docs.
"""

import repdefs
import rst
from rst2pyi import RST2PyI

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = "3.4.0"  # Version set by https://github.com/hlovatt/tag2ver


def btree(shed: RST2PyI) -> None:
    module_post_doc = f'''
from abc import abstractmethod
from typing import Protocol, Iterator, AnyStr, runtime_checkable, Optional, TypeVar

from uarray import array


@runtime_checkable
class _IOBase(Protocol):
    """
    A `Protocol` (structurally typed) for an IOStream.
    """

    __slots__ = ()

    @abstractmethod
    def __enter__(self) -> "_IOBase": ...
    
    @abstractmethod
    def __exit__(self) -> None: ...
    
    @abstractmethod
    def __next__(self) -> AnyStr: ...
    
    @abstractmethod
    def close(self) -> None: ...
    
    @abstractmethod
    def read(self, size: Optional[int] = -1) -> Optional[bytes]: ...
    
    @abstractmethod
    def readinto(self, b: _AnyWritableBuf) -> int: ...
    
    @abstractmethod
    def readline(self, size: int = -1) -> AnyStr: ...
    
    @abstractmethod
    def write(self, b: _AnyReadableBuf) -> int: ...
    
    @abstractmethod
    def flush(self) -> None: ...
    
    @abstractmethod
    def seek(self, offset: int, whence: int = 0) -> int: ...
    
    @abstractmethod
    def tell(self) -> int: ...


{repdefs.AnyWritableBuf}


{repdefs.AnyReadableBuf}
'''
    shed.module(
        name='btree',
        old='simple BTree database',
        post_doc=module_post_doc,
        end='Functions',
    )
    shed.pyi.doc += shed.extra_notes(end='Functions')
    shed.def_(
        old=r'.. function:: open(stream, *, flags=0, pagesize=0, cachesize=0, minkeypage=0)',
        new='''
def open(stream: _IOBase, /, *, flags: int = 0, pagesize: int = 0, cachesize: int = 0, minkeypage: int = 0) -> btree
''',
        indent=0
    )
    close_str = '.. method:: btree.close()'
    shed.class_(name='btree', end=close_str)
    shed.def_(
        old=close_str,
        new='def close(self) -> None',
    )
    shed.def_(
        old='.. method:: btree.flush()',
        new='def flush(self) -> None',
    )
    iter_str = '.. method:: btree.__iter__()'
    shed.defs_with_common_description(
        cmd='.. method:: btree.',
        old2new={
            '__getitem__(key)':
                'def __getitem__(self, key: bytes, /) -> bytes',
            'get(key, default=None, /)':
                'def get(self, key: bytes, default: Optional[bytes] = None, /) -> bytes',
            '__setitem__(key, val)':
                'def __setitem__(self, key: bytes, val: bytes, /) -> bytes',
            '__delitem__(key)':
                'def __delitem__(self, key: bytes, /) -> None',
            '__contains__(key)':
                'def __contains__(self, key: bytes, /) -> bool',
        },
        end=iter_str,
    )
    shed.def_(
        old=iter_str,
        new='def __iter__(self) -> Iterator[bytes]',
    )
    shed.defs_with_common_description(
        cmd='.. method:: btree.',
        old2new={
            'keys([start_key, [end_key, [flags]]])':
                '''
def keys(self, start_key: Optional[bytes] = None, end_key: Optional[bytes] = None, flags: int = 0, /) -> bytes
''',
            'values([start_key, [end_key, [flags]]])':
                '''
def values(self, start_key: Optional[bytes] = None, end_key: Optional[bytes] = None, flags: int = 0, /) -> bytes
''',
            'items([start_key, [end_key, [flags]]])':
                '''
def items(self, start_key: Optional[bytes] = None, end_key: Optional[bytes] = None, flags: int = 0, /) -> bytes
''',
        },
        end='Constants'
    )
    shed.consume_header_line(and_preceding_lines=True)
    shed.vars(class_var=None, end=None)
    shed.write()
