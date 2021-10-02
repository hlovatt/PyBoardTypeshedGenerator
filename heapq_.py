"""
Generate `pyi` from corresponding `rst` docs.
"""

import rst
from rst2pyi import RST2PyI

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = "6.0.0"  # Version set by https://github.com/hlovatt/tag2ver


def heapq(shed: RST2PyI) -> None:
    shed.module(
        name='heapq',
        old='heap queue algorithm',
        post_doc='''
from typing import TypeVar, Any, Final

_T: Final = TypeVar("_T")
''',
        end='Functions',
    )
    shed.consume_header_line(and_preceding_lines=True)
    shed.def_(
        old='.. function:: heappush(heap, item)',
        new='def heappush(heap: list[_T], item: _T, /) -> None',
        indent=0,
    )
    shed.def_(
        old='.. function:: heappop(heap)',
        new='def heappop(heap: list[_T], /) -> _T',
        indent=0,
    )
    shed.def_(
        old='.. function:: heapify(x)',
        new='def heapify(x: list[Any], /) -> None',
        indent=0,
    )
    shed.write(u_also=True)
