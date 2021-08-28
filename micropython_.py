"""
Generate `pyi` from corresponding `rst` docs.
"""

import rst
from rst2pyi import RST2PyI

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = "5.1.0"  # Version set by https://github.com/hlovatt/tag2ver


def micropython(shed: RST2PyI) -> None:
    shed.module(
        name='micropython',
        old='access and control MicroPython internals',
        post_doc=f'''
from typing import TypeVar, overload, Callable, Any

_T = TypeVar('_T')
''',
        end='Functions'
    )
    shed.consume_header_line(and_preceding_lines=True)
    shed.def_(
        old=R'.. function:: const(expr)',
        new=R'def const(expr: _T, /) -> _T',
        indent=0,
    )
    shed.def_(
        old=R'.. function:: opt_level([level])',
        new=[
            R'def opt_level() -> int',
            R'def opt_level(level: int, /) -> None',
        ],
        indent=0,
    )
    shed.def_(
        old=R'.. function:: alloc_emergency_exception_buf(size)',
        new=R'def alloc_emergency_exception_buf(size: int, /) -> None',
        indent=0,
    )
    shed.def_(
        old=R'.. function:: mem_info([verbose])',
        new=[
            R'def mem_info() -> None',
            R'def mem_info(verbose: Any, /) -> None',
        ],
        indent=0,
    )
    shed.def_(
        old=R'.. function:: qstr_info([verbose])',
        new=[
            R'def qstr_info() -> None',
            R'def qstr_info(verbose: bool, /) -> None',
        ],
        indent=0,
    )
    shed.def_(
        old=R'.. function:: stack_use()',
        new=R'def stack_use() -> int',
        indent=0,
    )
    cmd = R'.. function:: '
    kbd = cmd + R'kbd_intr(chr)'
    shed.defs_with_common_description(
        cmd=cmd,
        old2new={
            R'heap_lock()':
                R'def heap_lock() -> None',
            R'heap_unlock()':
                R'def heap_unlock() -> None',
            R'heap_locked()':
                R'def heap_locked() -> bool',
        },
        end=kbd,
        indent=0,
    )
    shed.def_(
        old=kbd,
        new=R'def kbd_intr(chr: int) -> None',
        indent=0,
    )
    shed.def_(
        old=R'.. function:: schedule(func, arg)',
        new=R'def schedule(func: Callable[[_T], None], arg: _T, /) -> None',
        indent=0,
    )
    shed.write()
