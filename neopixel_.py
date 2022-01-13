"""
Generate `pyi` from corresponding `rst` docs.
"""

import rst
from rst2pyi import RST2PyI

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = "7.5.2"  # Version set by https://github.com/hlovatt/tag2ver


def neopixel(shed: RST2PyI) -> None:
    shed.module(
        name=r"neopixel",
        old="control of WS2812 / NeoPixel LEDs",
        post_doc="""
from typing import Final

from machine import Pin

_Color: Final = tuple[int, int, int] | tuple[int, int, int, int]
""",
        end=r"class NeoPixel",
    )

    shed.consume_minuses_underline_line(and_preceding_lines=True)
    shed.class_(
        name=r"NeoPixel", end="Constructors",
    )
    shed.def_(
        old=r".. class:: NeoPixel(pin, n, *, bpp=3, timing=1)",
        new="def __init__(self, pin: Pin, n: int, /, *, bpp: int = 3, timing: int = 1)",
        end="Pixel access methods",
    )
    shed.def_(
        old=r".. method:: NeoPixel.fill(pixel)",
        new="def fill(self, pixel: _Color, /) -> None",
    )
    shed.def_(
        old=r".. method:: NeoPixel.__len__()", new="def __len__(self) -> int",
    )
    shed.def_(
        old=r".. method:: NeoPixel.__setitem__(index, val)",
        new="def __setitem__(self, index: int, val: _Color, /) -> None",
    )
    shed.def_(
        old=r".. method:: NeoPixel.__getitem__(index)",
        new="def __getitem__(self, index: int, /) -> _Color",
        end="Output methods",
    )
    shed.def_(
        old=r".. method:: NeoPixel.write()", new="def write(self) -> None",
    )

    shed.write()
