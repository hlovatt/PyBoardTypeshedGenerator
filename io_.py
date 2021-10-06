"""
Generate `pyi` from corresponding `rst` docs.
"""

import repdefs
import rst
from rst2pyi import RST2PyI

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = "6.1.0"  # Version set by https://github.com/hlovatt/tag2ver


def io(shed: RST2PyI) -> None:
    shed.module(
        name='io',
        old='input/output streams',
        post_doc=f'''
from typing import TypeVar, Final, Protocol, runtime_checkable, Literal, List
from typing import AnyStr, Optional, overload, Type
from types import TracebackType
from uarray import array

_T: Final = TypeVar("_T")

_OpenTextModeUpdating: Final = Literal[
    "r+",
    "+r",
    "rt+",
    "r+t",
    "+rt",
    "tr+",
    "t+r",
    "+tr",
    "w+",
    "+w",
    "wt+",
    "w+t",
    "+wt",
    "tw+",
    "t+w",
    "+tw",
    "a+",
    "+a",
    "at+",
    "a+t",
    "+at",
    "ta+",
    "t+a",
    "+ta",
    "x+",
    "+x",
    "xt+",
    "x+t",
    "+xt",
    "tx+",
    "t+x",
    "+tx",
]
_OpenTextModeWriting: Final = Literal["w", "wt", "tw", "a", "at", "ta", "x", "xt", "tx"]
_OpenTextModeReading: Final = Literal["r", "rt", "tr", "U", "rU", "Ur", "rtU", "rUt", "Urt", "trU", "tUr", "Utr"]
_OpenTextMode: Final = _OpenTextModeUpdating | _OpenTextModeWriting | _OpenTextModeReading

_OpenBinaryModeUpdating: Final = Literal[
    "rb+",
    "r+b",
    "+rb",
    "br+",
    "b+r",
    "+br",
    "wb+",
    "w+b",
    "+wb",
    "bw+",
    "b+w",
    "+bw",
    "ab+",
    "a+b",
    "+ab",
    "ba+",
    "b+a",
    "+ba",
    "xb+",
    "x+b",
    "+xb",
    "bx+",
    "b+x",
    "+bx",
]
_OpenBinaryModeWriting: Final = Literal["wb", "bw", "ab", "ba", "xb", "bx"]
_OpenBinaryModeReading: Final = Literal["rb", "br", "rbU", "rUb", "Urb", "brU", "bUr", "Ubr"]
_OpenBinaryMode: Final = _OpenBinaryModeUpdating | _OpenBinaryModeReading | _OpenBinaryModeWriting

_AnyStr_co = TypeVar("_AnyStr_co", str, bytes, covariant=True)
@runtime_checkable
class PathLike(Protocol[_AnyStr_co]):
    def __fspath__(self) -> _AnyStr_co: 
        ...

_StrOrBytesPath = str | bytes | PathLike[str] | PathLike[bytes]
_OpenFile = _StrOrBytesPath | int

{repdefs.ANY_WRITABLE_BUF}
{repdefs.ANY_READABLE_BUF}
{repdefs.IO_BASE}
''',
        end='Functions',
    )
    shed.def_(
        old=R".. function:: open(name, mode='r', **kwargs)",
        new=[
            'def open(name: _OpenFile, /, **kwargs) -> "TextIOWrapper"',
            'def open(name: _OpenFile, mode: _OpenTextMode = ..., /, **kwargs) -> "TextIOWrapper"',
            'def open(name: _OpenFile, mode: _OpenBinaryMode = ..., /, **kwargs) -> "FileIO"',
        ],
        indent=0,
        end='Classes'
    )
    shed.consume_header_line(and_preceding_lines=True)

    shed.class_(name='FileIO(_IOBase[bytes, "FileIO"])', end='..')
    shed.def_(
        old=R'.. class:: FileIO(...)',
        new='def __init__(self, name: _OpenFile, mode: str = ..., /, **kwargs)',
    )

    shed.class_(name='TextIOWrapper(_IOBase[str, "TextIOWrapper"])', end='..')
    shed.def_(
        old=R'.. class:: TextIOWrapper(...)',
        new='def __init__(self, name: _OpenFile, mode: str = ..., /, **kwargs)',
    )

    shed.class_(name='StringIO(_IOBase[str, "StringIO"])', end='..')
    # Add a harmless dummy-end line in to enable parsing of consecutive class definitions (which `def_` can't do!).
    last_line = shed.rst.pop_line()
    dummy_end = 'DUMMY END'
    shed.rst.push_line(dummy_end)
    shed.rst.push_line(' ')
    shed.rst.push_line(' ')
    shed.rst.push_line(last_line)
    shed.def_(
        old=R'.. class:: StringIO([string])',
        new=[
            'def _init__(self, string: str = "", /)',
            'def _init__(self, alloc_size: int, /)',
        ],
        extra_docs=['''
   In-memory file-like object for input/output.
   `StringIO` is used for text-mode I/O (similar to a normal file opened with "t" modifier).
   Initial contents can be specified with `string` parameter.
   
   `alloc_size` constructor creates an empty `StringIO` object, 
   pre-allocated to hold up to `alloc_size` number of bytes. 
   That means that writing that amount of bytes won't lead to reallocation of the buffer, 
   and thus won't hit out-of-memory situation or lead to memory fragmentation. 
   This constructor is a MicroPython extension and is recommended for usage only in special
   cases and in system-level libraries, not for end-user applications.

     .. admonition:: Difference to CPython
        :class: attention

        This constructor is a MicroPython extension.
'''],
        end=dummy_end
)
    shed.pyi.classes[-1].defs.append('''
   def getvalue(self) -> str:
      """Get the current contents of the underlying buffer which holds data."""
''')
    shed.consume_synopsis_line(name=dummy_end)

    shed.class_(name='BytesIO(_IOBase[bytes, "BytesIO"])', end='..')
    shed.def_(
        old=R'.. class:: BytesIO([string])',
        new=[
            'def _init__(self, string: bytes = "", /)',
            'def _init__(self, alloc_size: int, /)',
        ],
        extra_docs=['''
   `alloc_size` constructor creates an empty `BytesIO` object, 
   pre-allocated to hold up to `alloc_size` number of bytes. 
   That means that writing that amount of bytes won't lead to reallocation of the buffer, 
   and thus won't hit out-of-memory situation or lead to memory fragmentation. 
   This constructor is a MicroPython extension and is recommended for usage only in special
   cases and in system-level libraries, not for end-user applications.

     .. admonition:: Difference to CPython
        :class: attention

        This constructor is a MicroPython extension.
'''],
    )
    shed.def_(
        old=R'.. method:: getvalue()',
        new='def getvalue(self) -> bytes',
    )

    shed.consume_synopsis_line(R'.. class:: StringIO(alloc_size)', and_preceding_lines=True)
    shed.consume_synopsis_line(R'.. class:: BytesIO(alloc_size)', and_preceding_lines=True)
    shed.consume_synopsis_line(
        R'Create an empty `StringIO`/`BytesIO` object, preallocated to hold up',
        and_preceding_lines=True,
    )
    shed.consume_synopsis_line(
        R'to *alloc_size* number of bytes. That means that writing that amount',
        and_preceding_lines=True,
    )
    shed.consume_synopsis_line(
        R"of bytes won't lead to reallocation of the buffer, and thus won't hit",
        and_preceding_lines=True,
    )
    shed.consume_synopsis_line(
        R'out-of-memory situation or lead to memory fragmentation. These constructors',
        and_preceding_lines=True,
    )
    shed.consume_synopsis_line(
        R'are a MicroPython extension and are recommended for usage only in special',
        and_preceding_lines=True,
    )
    shed.consume_synopsis_line(
        R'cases and in system-level libraries, not for end-user applications.',
        and_preceding_lines=True,
    )
    shed.consume_synopsis_line(
        R'.. admonition:: Difference to CPython',
        and_preceding_lines=True,
    )
    shed.consume_synopsis_line(
        R':class: attention',
        and_preceding_lines=True,
    )
    shed.consume_synopsis_line(
        R'These constructors are a MicroPython extension.',
        and_preceding_lines=True,
    )

    shed.write(u_also=True)
