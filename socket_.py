"""
Generate `pyi` from corresponding `rst` docs.
"""
from typing import Final

import rst
from class_ import strip_leading_and_trailing_blank_lines
from rst2pyi import RST2PyI

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = "7.5.2"  # Version set by https://github.com/hlovatt/tag2ver


def socket(shed: RST2PyI) -> None:
    shed.module(
        name="socket",
        old="socket",
        post_doc=f"""
from typing import Final, Any, Literal, overload

from uio import AnyReadableBuf, AnyWritableBuf

_Address: Final = tuple[str, int] | tuple[str, int, int, int] | str
""",
        end="Functions",
    )

    shed.def_(
        old=r".. function:: socket(af=AF_INET, type=SOCK_STREAM, proto=IPPROTO_TCP, /)",
        new="""
def socket(
   af: int = "AF_INET", 
   type: int = "SOCK_STREAM", 
   proto: int = "IPPROTO_TCP", 
   /,
) -> "Socket"
""",
        indent=0,
    )
    shed.def_(
        old=r".. function:: getaddrinfo(host, port, af=0, type=0, proto=0, flags=0, /)",
        new="""
def getaddrinfo(
   host: str, 
   port: int, 
   af: int = 0, 
   type: int = 0, 
   proto: int = 0, 
   flags: int = 0, 
   /,
) -> list[tuple[int, int, int, str, tuple[str, int] | tuple[str, int, int, int]]]
""",
        indent=0,
    )
    shed.def_(
        pre_str="# noinspection PyUnresolvedReferences",
        old=r".. function:: inet_ntop(af, bin_addr)",
        new="def inet_ntop(af: int, bin_addr: bytes, /) -> str",
        indent=0,
    )
    shed.def_(
        pre_str="# noinspection PyUnresolvedReferences",
        old=r".. function:: inet_pton(af, txt_addr)",
        new="def inet_pton(af: int, txt_addr: str, /) -> bytes",
        indent=0,
        end="Constants",
    )

    shed.vars(
        old=[r".. data:: AF_INET", "AF_INET6"], class_var=None,
    )
    shed.vars(
        old=[r".. data:: SOCK_STREAM", "SOCK_DGRAM"], class_var=None,
    )
    shed.vars(
        old=[r".. data:: IPPROTO_UDP", "IPPROTO_TCP"], class_var=None,
    )
    shed.consume_containing_line(string=r".. data:: socket.SOL_*")
    sol_doc: Final = shed.extra_docs()
    shed.pyi.imports_vars_defs.append(
        '''
SOL_SOCKET: Final[int] = ...
"""
'''.strip()
    )
    shed.pyi.imports_vars_defs.extend(strip_leading_and_trailing_blank_lines(sol_doc))
    shed.pyi.imports_vars_defs.append('"""\n')
    shed.consume_containing_line(string=r".. data:: socket.SO_*")
    so_doc: Final = shed.extra_docs(end="Constants specific to WiPy:")
    shed.pyi.imports_vars_defs.append(
        '''
SO_REUSEADDR: Final[int] = ...
"""
'''.strip()
    )
    shed.pyi.imports_vars_defs.extend(strip_leading_and_trailing_blank_lines(so_doc))
    shed.pyi.imports_vars_defs.append('"""')
    sec_doc: Final = shed.extra_docs()
    shed.vars(
        old=r".. data:: IPPROTO_SEC",
        class_var=None,
        extra_docs=sec_doc,
        end="class socket",
    )

    shed.consume_equals_underline_line(and_preceding_lines=True)
    shed.consume_minuses_underline_line(and_preceding_lines=True)
    shed.class_(
        name=r"Socket",
        extra_docs=[
            """
   A unix like socket, for more information see module ``socket``'s description.
   
   The name, `Socket`, used for typing is not the same as the runtime name, `socket` (note lowercase `s`).
   The reason for this difference is that the runtime uses `socket` as both a class name and as a method name and
   this is not possible within code written entirely in Python and therefore not possible within typing code.
""".strip(
                "\n"
            )
        ],
        end=r".. method:: ",
    )
    shed.def_(
        old=r".. method:: socket.close()", new="def close(self) -> None",
    )
    shed.def_(
        old=r".. method:: socket.bind(address)",
        new="def bind(self, address: _Address | bytes, /) -> None",
    )
    shed.def_(
        old=r".. method:: socket.listen([backlog])",
        new="def listen(self, backlog: int = ..., /) -> None",
    )
    shed.def_(
        old=r".. method:: socket.accept()", new="def accept(self) -> None",
    )
    shed.def_(
        old=r".. method:: socket.connect(address)",
        new="def connect(self, address: _Address | bytes, /) -> None",
    )
    shed.def_(
        old=r".. method:: socket.send(bytes)",
        new="def send(self, bytes: AnyReadableBuf, /) -> int",
    )
    shed.def_(
        old=r".. method:: socket.sendall(bytes)",
        new="def sendall(self, bytes: AnyReadableBuf, /) -> None",
    )
    shed.def_(
        old=r".. method:: socket.recv(bufsize)",
        new="def recv(self, bufsize: int, /) -> bytes",
    )
    shed.def_(
        old=r".. method:: socket.sendto(bytes, address)",
        new="def sendto(self, bytes: AnyReadableBuf, address: _Address, /) -> int",
    )
    shed.def_(
        old=r".. method:: socket.recvfrom(bufsize)",
        new="def recvfrom(self, bufsize: int, /) -> tuple[bytes, Any]",
    )
    shed.def_(
        old=r".. method:: socket.setsockopt(level, optname, value)",
        new="def setsockopt(self, level: int, optname: int, value: AnyReadableBuf | int, /) -> None",
    )
    shed.def_(
        old=r".. method:: socket.settimeout(value)",
        new="def settimeout(self, value: float | None, /) -> None",
    )
    shed.def_(
        old=r".. method:: socket.setblocking(flag)",
        new="def setblocking(self, value: bool, /) -> None",
    )
    shed.def_(
        old=r".. method:: socket.makefile(mode='rb', buffering=0, /)",
        new=[
            "def makefile(self, mode: Literal['rb', 'wb', 'rwb'] = 'rb', buffering: int = 0, /) -> Socket",
            "def makefile(self, mode: str, buffering: int = 0, /) -> Socket",
        ],
    )
    shed.def_(
        old=r".. method:: socket.read([size])",
        new=["def read(self) -> bytes", "def read(self, size: int, /) -> bytes"],
    )
    shed.def_(
        old=r".. method:: socket.readinto(buf[, nbytes])",
        new=[
            "def readinto(self, buf: AnyWritableBuf, /) -> int | None",
            "def readinto(self, buf: AnyWritableBuf, nbytes: int, /) -> int | None",
        ],
    )
    shed.def_(
        old=r".. method:: socket.readline()", new="def readline(self) -> bytes",
    )
    shed.def_(
        old=r".. method:: socket.write(buf)",
        new="def write(self, buf: AnyReadableBuf, /) -> int | None",
    )

    err_doc: Final = shed.extra_notes(end=None)
    shed.pyi.doc.extend(err_doc)

    shed.write(u_also=True)
