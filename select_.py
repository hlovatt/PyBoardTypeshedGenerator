"""
Generate `pyi` from corresponding `rst` docs.
"""

import rst
from rst2pyi import RST2PyI

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = "6.2.0"  # Version set by https://github.com/hlovatt/tag2ver


def select(shed: RST2PyI) -> None:
    shed.module(
        name='select',
        old='wait for events on a set of streams',
        post_doc=f'''
from typing import Iterable, Any, Tuple, Final, Iterator

from uio import IOBase

POLLIN: Final[int] = ...
"""Data available for reading."""

POLLOUT: Final[int] = ...
"""More data can be written."""

POLLHUP: Final[int] = ...
"""Socket is no longer connected."""

POLLERR: Final[int] = ...
"""Socket got an asynchronous error."""
''',
        end='Functions',
    )

    shed.def_(
        old=R'.. function:: poll()',
        new='def poll() -> "Poll"',
        indent=0,
    )
    shed.def_(
        old=R'.. function:: select(rlist, wlist, xlist[, timeout])',
        new='''
def select(
   rlist: Iterable[Any], 
   wlist: Iterable[Any], 
   xlist: Iterable[Any], 
   timeout: int = -1, 
   /,
) -> list[Tuple[Any, int, Any, ...]]
''',
        indent=0,
    )
    # .. _class: Poll` is in `rst` file but not rendered by Sphinx (has no description either)!
    # It is ignored along with the `class ``Pol``` and `Method` headers in the `rst` file.
    shed.consume_header_line(and_preceding_lines=True)
    shed.consume_header2_line(and_preceding_lines=True)

    shed.class_(
        name='Poll',
        extra_docs=[
'''   The name, `Poll`, used for typing is not the same as the runtime name, `poll` (note lowercase `p`).
   The reason for this difference is that the runtime uses `poll` as both a class name and as a method name and
   this is not possible within code written entirely in Python and therefore not possible within typing code.'''
        ],
        end=R'.. method:: ',
    )
    shed.def_(
        old=R'.. method:: poll.register(obj[, eventmask])',
        new='def register(self, obj: IOBase, eventmask: int = POLLIN | POLLOUT, /) -> None',
    )
    shed.def_(
        old=R'.. method:: poll.unregister(obj)',
        new='def unregister(self, obj: IOBase, /) -> None',
    )
    shed.def_(
        old=R'.. method:: poll.modify(obj, eventmask)',
        new='def modify(self, obj: IOBase, eventmask: int, /) -> None',
    )
    shed.def_(
        old=R'.. method:: poll.poll(timeout=-1, /)',
        new='def poll(self, timeout: int = -1, /) -> list[Tuple[Any, int, Any, ...]]',
    )
    shed.def_(
        old=R'.. method:: poll.ipoll(timeout=-1, flags=0, /)',
        new='def ipoll(self, timeout: int = -1, flags: int = 0, /) -> Iterator[Tuple[Any, int, Any, ...]]',
    )

    shed.write(u_also=True)
