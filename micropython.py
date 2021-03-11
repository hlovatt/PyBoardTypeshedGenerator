"""
Generate `pyi` from corresponding `rst` docs.
"""

import rst
from rst2pyi import RST2PyI
import repdefs

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = "3.6.1"  # Version set by https://github.com/hlovatt/tag2ver


def micropython(shed: RST2PyI) -> None:
    shed.module(
        name='micropython',
        old='access and control MicroPython internals',
        post_doc=f'''
from typing import TypeVar, overload, Callable

_T = TypeVar('_T')
''',
        end='Functions'
    )
    shed.consume_header_line(and_preceding_lines=True)
    shed.def_(
        old=r'.. function:: const(expr)',
        new=r'def const(expr: _T, /) -> _T',
        indent=0,
    )
    shed.def_(
        old=r'.. function:: opt_level([level])',
        new=[
            r'def opt_level() -> int',
            r'def opt_level(level: int, /) -> None',
        ],
        indent=0,
    )
    shed.def_(
        old=r'.. function:: alloc_emergency_exception_buf(size)',
        new=r'def alloc_emergency_exception_buf(size: int, /) -> None',
        indent=0,
    )
    shed.def_(
        old=r'.. function:: mem_info([verbose])',
        new=[
            r'def mem_info() -> None',
            r'def mem_info(verbose: bool, /) -> None',
        ],
        indent=0,
    )
    shed.def_(
        old=r'.. function:: qstr_info([verbose])',
        new=[
            r'def qstr_info() -> None',
            r'def qstr_info(verbose: bool, /) -> None',
        ],
        indent=0,
    )
    shed.def_(
        old=r'.. function:: stack_use()',
        new=r'def stack_use() -> int',
        indent=0,
    )
    cmd = r'.. function:: '
    kbd = cmd + r'kbd_intr(chr)'
    shed.defs_with_common_description(
        cmd=cmd,
        old2new={
            r'heap_lock()':
                r'def heap_lock() -> None',
            r'heap_unlock()':
                r'def heap_unlock() -> None',
            r'heap_locked()':
                r'def heap_locked() -> bool',
        },
        end=kbd,
        indent=0,
    )
    shed.def_(
        old=kbd,
        new=r'def kbd_intr(chr: int) -> None',
        indent=0,
    )
    shed.def_(
        old=r'.. function:: schedule(func, arg)',
        new=r'def schedule(func: Callable[[_T], None], arg: _T, /) -> None',
        indent=0,
    )
    shed.write()
