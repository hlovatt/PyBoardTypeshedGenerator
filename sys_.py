"""
Generate `pyi` from corresponding `rst` docs.
"""

import rst
from rst2pyi import RST2PyI

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = "7.3.0"  # Version set by https://github.com/hlovatt/tag2ver


def sys(shed: RST2PyI) -> None:
    shed.module(
        name="sys",
        old="system specific functions",
        post_doc="""
from typing import Callable, Final, Literal, NoReturn

from uio import IOBase

class Implementation(tuple[str, tuple[int, int, int], int]):
    name: str
    version: tuple[int, int, int]
    mpy: int

class ModuleType:
    __class__: str
    __name__: str
""",
        end="Functions",
    )

    shed.def_(
        old=r".. function:: exit(retval=0, /)",
        new="def exit(retval: object = 0, /) -> NoReturn",
        indent=0,
    )
    shed.def_(
        old=r".. function:: atexit(func)",
        new="def atexit(func: Callable[[], None] | None, /) -> Callable[[], None] | None",
        indent=0,
    )
    shed.def_(
        old=r".. function:: print_exception(exc, file=sys.stdout, /)",
        new="def print_exception(exc: BaseException, file: IOBase[str] = 'stdout', /) -> None",
        indent=0,
        end="Constants",
    )

    shed.consume_minuses_underline_line(and_preceding_lines=True)
    shed.vars(
        old=r".. data:: argv", class_var=None, type_="list[str]",
    )
    shed.vars(
        old=r".. data:: byteorder", class_var=None, type_='Literal["little", "big"]',
    )
    shed.vars(
        old=r".. data:: implementation", class_var=None, type_="Implementation",
    )
    shed.vars(
        old=r".. data:: maxsize", class_var=None,
    )
    shed.vars(
        old=r".. data:: modules", class_var=None, type_="dict[str, ModuleType]",
    )
    shed.vars(
        old=r".. data:: path", class_var=None, type_="list[str]",
    )
    shed.vars(
        old=r".. data:: platform", class_var=None, type_="str",
    )
    shed.vars(
        old=r".. data:: stderr", class_var=None, type_="IOBase[str]",
    )
    shed.vars(
        old=r".. data:: stdin", class_var=None, type_="IOBase[str]",
    )
    shed.vars(
        old=r".. data:: stdout", class_var=None, type_="IOBase[str]",
    )
    shed.vars(
        old=r".. data:: version", class_var=None, type_="str",
    )
    shed.vars(
        old=r".. data:: version_info", class_var=None, type_="tuple[int, int, int]",
    )

    shed.write(u_also=True)
