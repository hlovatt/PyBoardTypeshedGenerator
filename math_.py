"""
Generate `pyi` from corresponding `rst` docs.
"""

import rst
from rst2pyi import RST2PyI

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = "7.5.3"  # Version set by https://github.com/hlovatt/tag2ver


def math(shed: RST2PyI) -> None:
    shed.module(
        name="math",
        old="mathematical functions",
        post_doc="from typing import SupportsFloat, Final",
        end="Functions",
    )
    shed.def_(
        old=".. function:: acos(x)",
        new="def acos(x: SupportsFloat, /) -> float",
        indent=0,
    )
    shed.def_(
        old=".. function:: acosh(x)",
        new="def acosh(x: SupportsFloat, /) -> float",
        indent=0,
    )
    shed.def_(
        old=".. function:: asin(x)",
        new="def asin(x: SupportsFloat, /) -> float",
        indent=0,
    )
    shed.def_(
        old=".. function:: asinh(x)",
        new="def asinh(x: SupportsFloat, /) -> float",
        indent=0,
    )
    shed.def_(
        old=".. function:: atan(x)",
        new="def atan(x: SupportsFloat, /) -> float",
        indent=0,
    )
    shed.def_(
        old=".. function:: atan2(y, x)",
        new="def atan2(y: SupportsFloat, x: SupportsFloat, /) -> float",
        indent=0,
    )
    shed.def_(
        old=".. function:: atanh(x)",
        new="def atanh(x: SupportsFloat, /) -> float",
        indent=0,
    )
    shed.def_(
        old=".. function:: ceil(x)",
        new="def ceil(x: SupportsFloat, /) -> int",
        indent=0,
    )
    shed.def_(
        old=".. function:: copysign(x, y)",
        new="def copysign(x: SupportsFloat, y: SupportsFloat, /) -> float",
        indent=0,
    )
    shed.def_(
        old=".. function:: cos(x)",
        new="def cos(x: SupportsFloat, /) -> float",
        indent=0,
    )
    shed.def_(
        old=".. function:: cosh(x)",
        new="def cosh(x: SupportsFloat, /) -> float",
        indent=0,
    )
    shed.def_(
        old=".. function:: degrees(x)",
        new="def degrees(x: SupportsFloat, /) -> float",
        indent=0,
    )
    shed.def_(
        old=".. function:: erf(x)",
        new="def erf(x: SupportsFloat, /) -> float",
        indent=0,
    )
    shed.def_(
        old=".. function:: erfc(x)",
        new="def erfc(x: SupportsFloat, /) -> float",
        indent=0,
    )
    shed.def_(
        old=".. function:: exp(x)",
        new="def exp(x: SupportsFloat, /) -> float",
        indent=0,
    )
    shed.def_(
        old=".. function:: expm1(x)",
        new="def expm1(x: SupportsFloat, /) -> float",
        indent=0,
    )
    shed.def_(
        old=".. function:: fabs(x)",
        new="def fabs(x: SupportsFloat, /) -> float",
        indent=0,
    )
    shed.def_(
        old=".. function:: floor(x)",
        new="def floor(x: SupportsFloat, /) -> int",
        indent=0,
    )
    shed.def_(
        old=".. function:: fmod(x, y)",
        new="def fmod(x: SupportsFloat, y: SupportsFloat, /) -> float",
        indent=0,
    )
    shed.def_(
        old=".. function:: frexp(x)",
        new="def frexp(x: SupportsFloat, /) -> tuple[float, int]",
        indent=0,
    )
    shed.def_(
        old=".. function:: gamma(x)",
        new="def gamma(x: SupportsFloat, /) -> float",
        indent=0,
    )
    shed.def_(
        old=".. function:: isfinite(x)",
        new="def isfinite(x: SupportsFloat, /) -> bool",
        indent=0,
    )
    shed.def_(
        old=".. function:: isinf(x)",
        new="def isinf(x: SupportsFloat, /) -> bool",
        indent=0,
    )
    shed.def_(
        old=".. function:: isnan(x)",
        new="def isnan(x: SupportsFloat, /) -> bool",
        indent=0,
    )
    shed.def_(
        pre_str="# noinspection PyShadowingNames",
        old=".. function:: ldexp(x, exp)",
        new="def ldexp(x: SupportsFloat, exp: int, /) -> float",
        indent=0,
    )
    shed.def_(
        old=".. function:: lgamma(x)",
        new="def lgamma(x: SupportsFloat, /) -> float",
        indent=0,
    )
    shed.def_(
        old=".. function:: log(x)",
        new="def log(x: SupportsFloat, /) -> float",
        indent=0,
    )
    shed.def_(
        old=".. function:: log10(x)",
        new="def log10(x: SupportsFloat, /) -> float",
        indent=0,
    )
    shed.def_(
        old=".. function:: log2(x)",
        new="def log2(x: SupportsFloat, /) -> float",
        indent=0,
    )
    shed.def_(
        old=".. function:: modf(x)",
        new="def modf(x: SupportsFloat, /) -> tuple[float, float]",
        indent=0,
    )
    shed.def_(
        old=".. function:: pow(x, y)",
        new="def pow(x: SupportsFloat, y: SupportsFloat, /) -> float",
        indent=0,
    )
    shed.def_(
        old=".. function:: radians(x)",
        new="def radians(x: SupportsFloat, /) -> float",
        indent=0,
    )
    shed.def_(
        old=".. function:: sin(x)",
        new="def sin(x: SupportsFloat, /) -> float",
        indent=0,
    )
    shed.def_(
        old=".. function:: sinh(x)",
        new="def sinh(x: SupportsFloat, /) -> float",
        indent=0,
    )
    shed.def_(
        old=".. function:: sqrt(x)",
        new="def sqrt(x: SupportsFloat, /) -> float",
        indent=0,
    )
    shed.def_(
        old=".. function:: tan(x)",
        new="def tan(x: SupportsFloat, /) -> float",
        indent=0,
    )
    shed.def_(
        old=".. function:: tanh(x)",
        new="def tanh(x: SupportsFloat, /) -> float",
        indent=0,
    )
    shed.def_(
        old=".. function:: trunc(x)",
        new="def trunc(x: SupportsFloat, /) -> float",
        indent=0,
    )
    shed.vars(
        old=".. data:: e", class_var=None, type_="float",
    )
    shed.vars(
        old=".. data:: pi", class_var=None, type_="float",
    )
    shed.write()
