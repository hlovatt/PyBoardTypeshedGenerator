"""
Generate `pyi` from corresponding `rst` docs.
"""
from typing import Final

import rst
from rst2pyi import RST2PyI

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = "7.5.0"  # Version set by https://github.com/hlovatt/tag2ver


def random(shed: RST2PyI) -> None:
    shed.module(
        name="random",
        old="random numbers",
        post_doc='''
from typing import TypeVar, runtime_checkable, Protocol, overload

_T = TypeVar('_T')

@runtime_checkable
class Subscriptable(Protocol[_T]):
    """A `Protocol` (structurally typed) for an object that is subscriptable and of finite length."""

    __slots__ = ()
    
    def __len__(self) -> int:
        """Number of elements, normally called via `len(x)` where `x` is an object that implements this protocol."""
        
    def __getitem__(self, index: int) -> _T:
        """
        Element at the given index, 
        normally called via `x[index]` where `x` is an object that implements this protocol.
        """
''',
        end="Functions for integers",
    )

    shed.def_(
        old=r".. function:: getrandbits(n)",
        new="def getrandbits(n: int, /) -> int",
        indent=0,
    )
    shed.def_(
        old=r".. function:: randint(a, b)",
        new="def randint(a: int, b: int, /) -> int",
        indent=0,
    )
    shed.defs_with_common_description(
        cmd=r".. function:: ",
        old2new={
            "randrange(stop)": """
@overload
def randrange(stop: int, /) -> int
""",
            "randrange(start, stop)": """
@overload
def randrange(start: int, stop: int, /) -> int
""",
            "randrange(start, stop[, step])": """
@overload
def randrange(start: int, stop: int, step: int, /) -> int
""",
        },
        indent=0,
        end="Functions for floats",
    )
    shed.def_(
        old=r".. function:: random()", new="def random() -> float", indent=0,
    )
    shed.def_(
        old=r".. function:: uniform(a, b)",
        new="def uniform(a: float, b: float) -> float",
        indent=0,
        end="Other Functions",
    )
    shed.def_(
        old=r".. function:: seed(n=None, /)",
        new="def seed(n: int | None = None, /) -> None",
        indent=0,
    )
    shed.def_(
        old=r".. function:: choice(sequence)",
        new="def choice(sequence: Subscriptable, /) -> None",
        indent=0,
    )

    shed.write()
