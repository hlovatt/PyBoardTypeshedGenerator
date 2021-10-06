"""
Generate `pyi` from corresponding `rst` docs.
"""
from typing import Final

import repdefs
import rst
from rst2pyi import RST2PyI

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = "6.2.0"  # Version set by https://github.com/hlovatt/tag2ver


def os(shed: RST2PyI) -> None:
    shed.module(
        name='os',
        old='basic "operating system" services',
        post_doc=f'''
from abc import abstractmethod
from types import TracebackType
from typing import Tuple, AnyStr, Final, TypeVar, runtime_checkable, Protocol
from typing import Optional, Type, List, overload, Literal

from uarray import array

_StrOrBytesT: Final = TypeVar('_StrOrBytesT', str, bytes)

class _PathLike(Protocol[_StrOrBytesT]):
    @abstractmethod
    def __fspath__(self) -> _StrOrBytesT:
        """Return the file system path representation of the object, preferably as a `str`."""
    
_AnyPath: Final = str | bytes | _PathLike[str] | _PathLike[bytes]
_FdOrAnyPath: Final = int | _AnyPath

{repdefs.ANY_READABLE_BUF}
{repdefs.ANY_WRITABLE_BUF}
{repdefs.IO_BASE}
''',
        end='General functions',
    )

    shed.def_(
        old=R'.. function:: uname()',
        new='def uname() -> Tuple[str, str, str, str, str]',
        indent=0,
    )
    shed.def_(
        old=R'.. function:: urandom(n)',
        new='def urandom(n: int, /) -> bytes',
        end='Filesystem access',
        indent=0,
    )

    shed.def_(
        old=R'.. function:: chdir(path)',
        new='def chdir(path: _FdOrAnyPath, /) -> None',
        indent=0,
    )
    shed.def_(
        old=R'.. function:: getcwd()',
        new='def getcwd() -> str',
        indent=0,
    )
    shed.def_(
        old=R'.. function:: ilistdir([dir])',
        new=[
            'def ilistdir() -> List[Tuple[str, int, int] | Tuple[str, int, int, int]]',
            'def ilistdir(dir: int, /) -> List[Tuple[str, int, int] | Tuple[str, int, int, int]]',
            'def ilistdir(dir: str, /) -> List[Tuple[str, int, int] | Tuple[str, int, int, int]]',
            'def ilistdir(dir: bytes, /) -> List[Tuple[bytes, int, int] | Tuple[bytes, int, int, int]]',
            'def ilistdir(dir: _PathLike[str], /) -> List[Tuple[str, int, int] | Tuple[str, int, int, int]]',
            'def ilistdir(dir: _PathLike[bytes], /) -> List[Tuple[bytes, int, int] | Tuple[bytes, int, int, int]]',
        ],
        indent=0,
    )
    shed.def_(
        old=R'.. function:: listdir([dir])',
        new=[
            'def listdir() -> List[str]',
            'def listdir(dir: int, /) -> List[str]',
            'def listdir(dir: str, /) -> List[str]',
            'def listdir(dir: bytes, /) -> List[bytes]',
            'def listdir(dir: _PathLike[str], /) -> List[str]',
            'def listdir(dir: _PathLike[bytes], /) -> List[bytes]',
        ],
        indent=0,
    )
    shed.def_(
        old=R'.. function:: mkdir(path)',
        new='def mkdir(path: _AnyPath, /) -> None',
        indent=0,
    )
    shed.def_(
        old=R'.. function:: remove(path)',
        new='def remove(path: _AnyPath, /) -> None',
        indent=0,
    )
    shed.def_(
        old=R'.. function:: rmdir(path)',
        new='def rmdir(path: _AnyPath, /) -> None',
        indent=0,
    )
    shed.def_(
        old=R'.. function:: rename(old_path, new_path)',
        new='def rename(old_path: _AnyPath, new_path: _AnyPath, /) -> None',
        indent=0,
    )
    shed.def_(
        old=R'.. function:: stat(path)',
        new='def stat(path: _FdOrAnyPath, /) -> Tuple[int, int, int, int, int, int, int, int, int, int]',
        indent=0,
    )
    shed.def_(
        old=R'.. function:: statvfs(path)',
        new='def statvfs(path: _FdOrAnyPath, /) -> Tuple[int, int, int, int, int, int, int, int, int, int]',
        indent=0,
    )
    shed.def_(
        old=R'.. function:: sync()',
        new='def sync() -> None',
        end='Terminal redirection and duplication',
        indent=0,
    )
    shed.def_(
        old=R'.. function:: dupterm(stream_object, index=0, /)',
        new='def dupterm(stream_object: IOBase | None, index: int = 0, /) -> IOBase | None',
        end='Filesystem mounting',
        indent=0,
    )

    mount_def = R'.. function:: mount(fsobj, mount_point, *, readonly)'
    extra_mount_docs: Final = shed.extra_docs(end=mount_def)
    shed.def_(
        old=mount_def,
        new='def mount(fsobj: "AbstractBlockDev", mount_point: str, /, *, readonly: bool = False) -> IOBase | None',
        extra_docs=extra_mount_docs,
        indent=0,
    )
    shed.def_(
        old=R'.. function:: umount(mount_point)',
        new='def umount(mount_point: str, /) -> None',
        indent=0,
    )

    vfs_fat_class: Final = R'.. class:: VfsFat(block_dev)'
    shed.class_(name='VfsFat("AbstractBlockDev")', end=vfs_fat_class)
    shed.def_(
        old=vfs_fat_class,
        new='def __init__(self, block_dev: "AbstractBlockDev", /)',
    )
    shed.def_(
        old=R'.. staticmethod:: mkfs(block_dev)',
        new='''
@staticmethod
def mkfs(block_dev: "AbstractBlockDev", /) -> None
''',
    )

    vfs_lfs1_class: Final = R'.. class:: VfsLfs1(block_dev, readsize=32, progsize=32, lookahead=32)'
    shed.class_(name='VfsLfs1("AbstractBlockDev")', end=vfs_lfs1_class)
    shed.def_(
        old=vfs_lfs1_class,
        new='''
def __init__(
   self, 
   block_dev: "AbstractBlockDev", 
   readsize: int = 32, 
   progsize: int = 32, 
   lookahead: int = 32, 
   /,
)
''',
    )
    shed.def_(
        old=R'.. staticmethod:: mkfs(block_dev, readsize=32, progsize=32, lookahead=32)',
        new='''
@staticmethod
def mkfs(
   block_dev: "AbstractBlockDev", 
   readsize: int = 32, 
   progsize: int = 32, 
   lookahead: int = 32, 
   /,
) -> None
''',
    )
    vfs_lfs2_class: Final = R'.. class:: VfsLfs2(block_dev, readsize=32, progsize=32, lookahead=32, mtime=True)'
    extra_note_lfs1: Final = shed.extra_notes(end=vfs_lfs2_class)
    shed.pyi.classes[-1].doc.extend(extra_note_lfs1)

    shed.class_(name='VfsLfs2("AbstractBlockDev")', end=vfs_lfs2_class)
    shed.def_(
        old=vfs_lfs2_class,
        new='''
def __init__(
   self, 
   block_dev: "AbstractBlockDev", 
   readsize: int = 32, 
   progsize: int = 32, 
   lookahead: int = 32, 
   mtime: bool = True,
   /,
)
''',
    )
    shed.def_(
        old=R'.. staticmethod:: mkfs(block_dev, readsize=32, progsize=32, lookahead=32)',
        new='''
@staticmethod
def mkfs(
   block_dev: "AbstractBlockDev", 
   readsize: int = 32, 
   progsize: int = 32, 
   lookahead: int = 32, 
   mtime: bool = True,
   /,
) -> None
''',
    )
    unused_ref = '.. _littlefs v1 filesystem format: https://github.com/ARMmbed/littlefs/tree/v1'
    extra_note_lfs2: Final = shed.extra_notes(end=unused_ref)
    shed.pyi.classes[-1].doc.extend(extra_note_lfs2)

    shed.consume_name_line(name=unused_ref)
    shed.consume_name_line(name='.. _littlefs v2 filesystem format: https://github.com/ARMmbed/littlefs')
    shed.consume_name_line(name='.. _littlefs issue 295: https://github.com/ARMmbed/littlefs/issues/295')
    shed.consume_name_line(name='.. _littlefs issue 347: https://github.com/ARMmbed/littlefs/issues/347')

    vfs_abd_class: Final = R'.. class:: AbstractBlockDev(...)'
    shed.class_(
        pre_str='@runtime_checkable',
        name='AbstractBlockDev(Protocol)',
        end=vfs_abd_class,
    )
    shed.def_(
        old=vfs_abd_class,
        new='def __init__(self)',
    )
    shed.defs_with_common_description(
        cmd=R'    .. method:: ',
        old2new={
            R'readblocks(block_num, buf)':
'''
@overload
def readblocks(self, block_num: int, buf: bytearray, /) -> None
''',
            R'readblocks(block_num, buf, offset)':
'''
@overload
def readblocks(self, block_num: int, buf: bytearray, offset: int, /) -> None
''',
        }
    )
    shed.defs_with_common_description(
        cmd=R'    .. method:: ',
        old2new={
            R'writeblocks(block_num, buf)':
'''
@overload
def writeblocks(self, block_num: int, buf: bytes | bytearray, /) -> None
''',
            R'writeblocks(block_num, buf, offset)':
'''
@overload
def writeblocks(self, block_num: int, buf: bytes | bytearray, offset: int, /) -> None
''',
        }
    )
    shed.def_(
        old=R'.. method:: ioctl(op, arg)',
        new=[
            'def ioctl(self, op: int, arg: int) -> int | None',
            'def ioctl(self, op: Literal[4, 5], arg: int) -> int',
            'def ioctl(self, op: Literal[1, 2, 3, 6], arg: int) -> int | None',
        ],
    )

    shed.write(u_also=True)
