"""
Generate `pyi` from corresponding `rst` docs.
"""

import rst
from rst2pyi import RST2PyI

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = "7.5.2"  # Version set by https://github.com/hlovatt/tag2ver


def time(shed: RST2PyI) -> None:
    shed.module(
        name="time",
        old="time related functions",
        post_doc="""
from typing import Final, TypeVar

class _TicksMs:
   ...

class _TicksUs:
   ...

class _TicksCPU:
   ...

_Ticks: Final = TypeVar("_Ticks", _TicksMs, _TicksUs, _TicksCPU, int)
""",
        end="Functions",
    )

    shed.consume_minuses_underline_line(and_preceding_lines=True)
    shed.defs_with_common_description(
        cmd=".. function:: ",
        old2new={
            r"gmtime([secs])": "def gmtime(secs: int | None = None, /) -> tuple[int, int, int, int, int, int, int, int]",
            r"localtime([secs])": "def localtime(secs: int | None = None, /) -> tuple[int, int, int, int, int, int, int, int]",
        },
        indent=0,
    )
    shed.def_(
        old=r".. function:: mktime()",
        new="def mktime(local_time: tuple[int, int, int, int, int, int, int, int], /) -> int",
        indent=0,
    )
    shed.def_(
        old=r".. function:: sleep(seconds)",
        new="def sleep(seconds: float, /) -> None",
        indent=0,
    )
    shed.def_(
        old=r".. function:: sleep_ms(ms)",
        new="def sleep_ms(ms: int, /) -> None",
        indent=0,
    )
    shed.def_(
        old=r".. function:: sleep_us(us)",
        new="def sleep_us(us: int, /) -> None",
        indent=0,
    )
    shed.def_(
        old=r".. function:: ticks_ms()", new="def ticks_ms() -> _TicksMs", indent=0,
    )
    shed.def_(
        old=r".. function:: ticks_us()", new="def ticks_us() -> _TicksUs", indent=0,
    )
    shed.def_(
        old=r".. function:: ticks_cpu()", new="def ticks_cpu() -> _TicksCPU", indent=0,
    )
    shed.def_(
        old=r".. function:: ticks_add(ticks, delta)",
        new="def ticks_add(ticks: _Ticks, delta: int, /) -> _Ticks",
        indent=0,
    )
    shed.def_(
        old=r".. function:: ticks_diff(ticks1, ticks2)",
        new="def ticks_diff(ticks1: _Ticks, ticks2: _Ticks, /) -> int",
        indent=0,
    )
    shed.def_(
        old=r".. function:: time()", new="def time() -> int", indent=0,
    )
    shed.def_(
        old=r".. function:: time_ns()", new="def time_ns() -> int", indent=0,
    )

    shed.write(u_also=True)
