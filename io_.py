"""
Generate `pyi` from corresponding `rst` docs.
"""

import rst
from rst2pyi import RST2PyI

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = "7.5.0"  # Version set by https://github.com/hlovatt/tag2ver


def io(shed: RST2PyI) -> None:
    shed.module(
        name="io",
        old="input/output streams",
        post_doc=f'''
from types import TracebackType
from typing import TypeVar, Final, Protocol, runtime_checkable, Literal
from typing import AnyStr, overload, Type

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

AnyStr_co: Final = TypeVar("AnyStr_co", str, bytes, covariant=True)
@runtime_checkable
class PathLike(Protocol[AnyStr_co]):
    def __fspath__(self) -> AnyStr_co: 
        ...

StrOrBytesPath: Final = str | bytes | PathLike[str] | PathLike[bytes]
_OpenFile: Final = StrOrBytesPath | int

AnyReadableBuf: Final = TypeVar('AnyReadableBuf', bytearray, array, memoryview, bytes)
"""
Type that allows bytearray, array, memoryview, or bytes, 
but only one of these and not a mixture in a single declaration.
"""

AnyWritableBuf: Final = TypeVar('AnyWritableBuf', bytearray, array, memoryview)
"""
Type that allows bytearray, array, or memoryview, but only one of these and not a mixture in a single declaration.
"""

_Self: Final = TypeVar('_Self')  # The type that extends `IOBase`.

@runtime_checkable
class IOBase(Protocol[AnyStr, _Self]):
    """A `Protocol` (structurally typed) for an IOStream."""

    __slots__ = ()
    
    def __enter__(self) -> _Self:
        """
        Called on entry to a `with` block.
        The `with` statement will bind this method’s return value to the target(s) specified in the `as` clause 
        of the statement, if any.
        """
        
    def __exit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> bool | None:
        """
        Called on exit of a `with` block.
        The parameters describe the exception that caused the context to be exited. 
        If the context was exited without an exception, all three arguments will be `None`.

        If an exception is supplied, and the method wishes to suppress the exception 
        (i.e., prevent it from being propagated), it should return a true value. 
        Otherwise, the exception will be processed normally upon exit from this method.

        *Note* that `__exit__()` methods should not re-raise the passed-in exception; 
        this is the caller’s responsibility.
        """
        
    def __next__(self) -> AnyStr:
        """
        Next string.
        """
    
    def __iter__(self) -> _Self:
        """
        Start new iteration.
        """

    def close(self) -> None:
        """
        Flushes the write buffers and closes the IO stream; best not called directly, use a `with` block instead.
        Calling `f.close()` without using a `with` block might result in content not being completely written to the 
        disk, even if the program exits successfully.
        A closed file cannot be read or written any more. 
        Any operation which requires that the file be open will raise a `ValueError` after the file has been closed. 
        Calling `f.close()` more than once is allowed.
        """

    def flush(self) -> None:
        """
        Flushes the write buffers of the IO stream.
        `flush()` does not necessarily write the file’s data to disk. 
        Use `f.flush()` followed by `os.sync()` to ensure this behavior.
        
        This method does nothing for read-only and non-blocking streams.
        """

    def read(self, size: int | None = -1) -> AnyStr | None:
        """
        Read up to `size` bytes from the object and return them as a `str` (text file) or `bytes` (binary file). 
        As a convenience, if `size` is unspecified or -1, all bytes until EOF are returned. 
        Otherwise, only one system call is ever made. 
        Fewer than `size` bytes may be returned if the operating system call returns fewer than `size` bytes.

        If 0 bytes are returned, and `size` was not 0, this indicates end of file. 
        If `self` is in non-blocking mode and no bytes are available, `None` is returned.
        """

    def readinto(self, b: AnyWritableBuf) -> int | None:
        """
        Read bytes into a pre-allocated, writable bytes-like object b, and return the number of bytes read. 
        For example, b might be a bytearray. 
        
        If `self` is in non-blocking mode and no bytes are available, `None` is returned.
        """

    def readline(self, size: int = -1) -> AnyStr:
        """
        Read and return, as a `str` (text file) or `bytes` (binary file), one line from the stream. 
        If size is specified, at most size bytes will be read.
        
        The line terminator is always `b'\n'` for binary files; 
        for text files, the newline argument to `open()` can be used to select the line terminator(s) recognized.
        """

    def readlines(self, hint: int | None = -1) -> list[AnyStr]:
        """
        Read and return a list of lines, as a `list[str]` (text file) or `list[bytes]` (binary file), from the stream. 
        `hint` can be specified to control the number of lines read: 
        no more lines will be read if the total size (in bytes/characters) of all lines so far exceeds `hint`.

        `hint` values of 0 or less, as well as `None`, are treated as no hint.
        The line terminator is always `b'\n'` for binary files; 
        for text files, the newline argument to `open()` can be used to select the line terminator(s) recognized.

        *Note* that it’s already possible to iterate on file objects using `for line in file: ...` 
        without calling `file.readlines()`.
        """

    def write(self, b: AnyReadableBuf) -> int | None:
        """
        Write the given bytes-like object, `b`, to the underlying raw stream, and return the number of bytes written. 
        This can be less than the length of `b` in bytes, depending on specifics of the underlying raw stream, 
        and especially if it is in non-blocking mode. 
        `None` is returned if the raw stream is set not to block and no single byte could be readily written to it. 
        
        The caller may release or mutate `b` after this method returns, 
        so the implementation only access `b` during the method call.
        """

    def seek(self, offset: int, whence: int = 0) -> int:
        """
        Change the stream position to the given byte `offset`. 
        `offset` is interpreted relative to the position indicated by `whence`.
        The default value for whence is 0. 
        
        Values for whence are:

          * 0 – start of the stream (the default); offset should be zero or positive.
          * 1 – current stream position; offset may be negative.
          * 2 – end of the stream; offset is usually negative.
        
        Returns the new absolute position.
        """

    def tell(self) -> int:
        """
        Return the current stream position.
        """
''',
        end="Functions",
    )
    shed.def_(
        old=r".. function:: open(name, mode='r', **kwargs)",
        new=[
            'def open(name: _OpenFile, /, **kwargs) -> "TextIOWrapper"',
            'def open(name: _OpenFile, mode: _OpenTextMode = ..., /, **kwargs) -> "TextIOWrapper"',
            'def open(name: _OpenFile, mode: _OpenBinaryMode = ..., /, **kwargs) -> "FileIO"',
        ],
        indent=0,
        end="Classes",
    )
    shed.consume_minuses_underline_line(and_preceding_lines=True)

    shed.class_(
        name='FileIO(IOBase[bytes, "FileIO"])',
        extra_docs=["Bytes stream from a file."],
        end="..",
    )
    shed.def_(
        old=r".. class:: FileIO(...)",
        new="def __init__(self, name: _OpenFile, mode: str = ..., /, **kwargs)",
    )

    shed.class_(
        name='TextIOWrapper(IOBase[str, "TextIOWrapper"])',
        extra_docs=["Str stream from a file."],
        end="..",
    )
    shed.def_(
        old=r".. class:: TextIOWrapper(...)",
        new="def __init__(self, name: _OpenFile, mode: str = ..., /, **kwargs)",
    )

    shed.class_(
        name='StringIO(IOBase[str, "StringIO"])',
        extra_docs=["Str stream from a str (wrapper)."],
        end="..",
    )
    # Add a harmless dummy-end line in to enable parsing of consecutive class definitions (which `def_` can't do!).
    last_line = shed.rst.pop_line()
    dummy_end = "DUMMY END"
    shed.rst.push_line(dummy_end)
    shed.rst.push_line(" ")
    shed.rst.push_line(" ")
    shed.rst.push_line(last_line)
    shed.def_(
        old=r".. class:: StringIO([string])",
        new=[
            'def __init__(self, string: str = "", /)',
            "def __init__(self, alloc_size: int, /)",
        ],
        extra_docs=[
            """
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
"""
        ],
        end=dummy_end,
    )
    shed.pyi.classes[-1].defs.append(
        '''
   def getvalue(self) -> str:
      """Get the current contents of the underlying buffer which holds data."""
'''
    )
    shed.consume_containing_line(string=dummy_end)

    shed.class_(
        name='BytesIO(IOBase[bytes, "BytesIO"])',
        extra_docs=["Bytes stream from a bytes array (wrapper)."],
        end="..",
    )
    shed.def_(
        old=r".. class:: BytesIO([string])",
        new=[
            'def __init__(self, string: bytes = "", /)',
            "def __init__(self, alloc_size: int, /)",
        ],
        extra_docs=[
            """
   `alloc_size` constructor creates an empty `BytesIO` object, 
   pre-allocated to hold up to `alloc_size` number of bytes. 
   That means that writing that amount of bytes won't lead to reallocation of the buffer, 
   and thus won't hit out-of-memory situation or lead to memory fragmentation. 
   This constructor is a MicroPython extension and is recommended for usage only in special
   cases and in system-level libraries, not for end-user applications.

     .. admonition:: Difference to CPython
        :class: attention

        This constructor is a MicroPython extension.
"""
        ],
    )
    shed.def_(
        old=r".. method:: getvalue()", new="def getvalue(self) -> bytes",
    )

    shed.consume_containing_line(
        r".. class:: StringIO(alloc_size)", and_preceding_lines=True,
    )
    shed.consume_containing_line(
        r".. class:: BytesIO(alloc_size)", and_preceding_lines=True,
    )
    shed.consume_containing_line(
        r"Create an empty `StringIO`/`BytesIO` object, preallocated to hold up",
        and_preceding_lines=True,
    )
    shed.consume_containing_line(
        r"to *alloc_size* number of bytes. That means that writing that amount",
        and_preceding_lines=True,
    )
    shed.consume_containing_line(
        r"of bytes won't lead to reallocation of the buffer, and thus won't hit",
        and_preceding_lines=True,
    )
    shed.consume_containing_line(
        r"out-of-memory situation or lead to memory fragmentation. These constructors",
        and_preceding_lines=True,
    )
    shed.consume_containing_line(
        r"are a MicroPython extension and are recommended for usage only in special",
        and_preceding_lines=True,
    )
    shed.consume_containing_line(
        r"cases and in system-level libraries, not for end-user applications.",
        and_preceding_lines=True,
    )
    shed.consume_containing_line(
        r".. admonition:: Difference to CPython", and_preceding_lines=True,
    )
    shed.consume_containing_line(
        r":class: attention", and_preceding_lines=True,
    )
    shed.consume_containing_line(
        r"These constructors are a MicroPython extension.", and_preceding_lines=True,
    )

    shed.write(u_also=True)
