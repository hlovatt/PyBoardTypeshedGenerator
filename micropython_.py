"""
Generate `pyi` from corresponding `rst` docs.
"""

import rst
from rst2pyi import RST2PyI

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = "7.2.0"  # Version set by https://github.com/hlovatt/tag2ver


def micropython(shed: RST2PyI) -> None:
    shed.module(
        name="micropython",
        old="access and control MicroPython internals",
        post_doc=f'''
from typing import TypeVar, overload, Callable, Any, Final

_T: Final = TypeVar('_T')
_F: Final = TypeVar("_F", bound=Callable[..., Any])

def native(func: _F) -> _F:
   """
   This causes the MicroPython compiler to emit unoptimised native CPU opcodes
   rather than bytecode (normal) or optimised opcodes (viper) and is an optimisation,
   for more information see 
   https://docs.micropython.org/en/latest/reference/speed_python.html#the-native-code-emitter.
   """

def viper(func: _F) -> _F:
   """
   This causes the MicroPython compiler to emit optimised native CPU opcodes based on special typehints
   rather than bytecode (normal) or unoptimised opcodes (native) and is an optimisation,
   for more information see 
   https://docs.micropython.org/en/latest/reference/speed_python.html#the-viper-code-emitter.
   """
''',
        end="Functions",
    )
    shed.consume_minuses_underline_line(and_preceding_lines=True)
    shed.def_(
        old=r".. function:: const(expr)", new="def const(expr: _T, /) -> _T", indent=0,
    )
    shed.def_(
        old=r".. function:: opt_level([level])",
        new=["def opt_level() -> int", "def opt_level(level: int, /) -> None"],
        indent=0,
    )
    shed.def_(
        old=r".. function:: alloc_emergency_exception_buf(size)",
        new="def alloc_emergency_exception_buf(size: int, /) -> None",
        indent=0,
    )
    shed.def_(
        old=r".. function:: mem_info([verbose])",
        new=["def mem_info() -> None", "def mem_info(verbose: Any, /) -> None"],
        indent=0,
    )
    shed.def_(
        old=r".. function:: qstr_info([verbose])",
        new=["def qstr_info() -> None", "def qstr_info(verbose: bool, /) -> None"],
        indent=0,
    )
    shed.def_(
        old=r".. function:: stack_use()", new="def stack_use() -> int", indent=0,
    )
    cmd = r".. function:: "
    kbd = cmd + r"kbd_intr(chr)"
    shed.defs_with_common_description(
        cmd=cmd,
        old2new={
            r"heap_lock()": "def heap_lock() -> None",
            r"heap_unlock()": "def heap_unlock() -> None",
            r"heap_locked()": "def heap_locked() -> bool",
        },
        end=kbd,
        indent=0,
    )
    shed.def_(
        old=kbd, new="def kbd_intr(chr: int) -> None", indent=0,
    )
    shed.def_(
        old=r".. function:: schedule(func, arg)",
        new="def schedule(func: Callable[[_T], None], arg: _T, /) -> None",
        indent=0,
    )
    shed.write()
