"""
Repeated typeshed definitions;
definitions needed by more than one typeshed, i.e. common to multiple typesheds.
"""

import rst

__author__ = rst.__author__
__copyright_ = rst.__copyright__
__license__ = rst.__license__
__version__ = "4.0.0"  # Version set by https://github.com/hlovatt/tag2ver

AbstractBlockDev = '''
@runtime_checkable
class _AbstractBlockDev(Protocol):
    """
    A `Protocol` (structurally typed) with the defs needed by 
    `usb_mode` argument `msc`.
    """

    __slots__ = ()

    @abstractmethod
    def readblocks(self, blocknum: int, buf: bytes, offset: int = 0, /) -> None: ... 

    @abstractmethod
    def writeblocks(self, blocknum: int, buf: bytes, offset: int = 0, /) -> None: ...

    @abstractmethod
    def ioctl(self, op: int, arg: int) -> Optional[int]: ...
'''

AnyWritableBuf = '''
_AnyWritableBuf = TypeVar('_AnyWritableBuf', bytearray, array, memoryview)
"""
Type that allows bytearray, array, or memoryview, but only one of these and not a mixture in a single declaration.
"""
'''

AnyReadableBuf = '''
_AnyReadableBuf = TypeVar('_AnyReadableBuf', bytearray, array, memoryview, bytes)
"""
Type that allows bytearray, array, memoryview, or bytes, 
but only one of these and not a mixture in a single declaration.
"""
'''
