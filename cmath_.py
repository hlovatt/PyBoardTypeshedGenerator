"""
Generate `pyi` from corresponding `rst` docs.
"""

import rst
from rst2pyi import RST2PyI

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = "7.5.3"  # Version set by https://github.com/hlovatt/tag2ver


def cmath(shed: RST2PyI) -> None:
    shed.module(
        name="cmath",
        old="mathematical functions for complex numbers",
        post_doc="""
from typing import SupportsComplex, SupportsFloat, Final

_C: Final = SupportsFloat | SupportsComplex
""",
        end="Functions",
    )
    shed.def_(
        old=".. function:: cos(z)", new="def cos(z: _C, /) -> complex", indent=0,
    )
    shed.def_(
        old=".. function:: exp(z)", new="def exp(z: _C, /) -> complex", indent=0,
    )
    shed.def_(
        old=".. function:: log(z)", new="def log(z: _C, /) -> complex", indent=0,
    )
    shed.def_(
        old=".. function:: log10(z)", new="def log10(z: _C, /) -> complex", indent=0,
    )
    shed.def_(
        old=".. function:: phase(z)", new="def phase(z: _C, /) -> float", indent=0,
    )
    shed.def_(
        old=".. function:: polar(z)",
        new="def polar(z: _C, /) -> tuple[float, float]",
        indent=0,
    )
    shed.def_(
        old=".. function:: rect(r, phi)",
        new="def rect(r: float, phi: float, /) -> complex",
        indent=0,
    )
    shed.def_(
        old=".. function:: sin(z)", new="def sin(z: _C, /) -> complex", indent=0,
    )
    shed.def_(
        old=".. function:: sqrt(z)",
        new="def sqrt(z: _C, /) -> complex",
        end="Constants",
        indent=0,
    )
    shed.vars(
        old=".. data:: e", class_var=None, type_="float",
    )
    shed.vars(
        old=".. data:: pi", class_var=None, type_="float",
    )
    shed.write()
