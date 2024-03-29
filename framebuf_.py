"""
Generate `pyi` from corresponding `rst` docs.
"""

import rst
from rst2pyi import RST2PyI

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = "7.5.3"  # Version set by https://github.com/hlovatt/tag2ver


def framebuf(shed: RST2PyI) -> None:
    shed.module(
        name="framebuf",
        old="Frame buffer manipulation",
        post_doc=f"""
from typing import overload, Final

from uio import AnyWritableBuf
""",
        end="class FrameBuffer",
    )
    shed.consume_minuses_underline_line(and_preceding_lines=True)
    shed.class_(
        name="FrameBuffer", end="Constructors",
    )
    shed.def_(
        old=r".. class:: FrameBuffer(buffer, width, height, format, stride=width, /)",
        new="def __init__(self, buffer: AnyWritableBuf, width: int, height: int, format: int, stride: int = ..., /)",
    )
    shed.def_(
        old=r".. method:: FrameBuffer.fill(c)", new="def fill(self, c: int, /) -> None",
    )
    shed.def_(
        old=r".. method:: FrameBuffer.pixel(x, y[, c])",
        new=[
            "def pixel(self, x: int, y: int, /) -> int",
            "def pixel(self, x: int, y: int, c: int, /) -> None",
        ],
    )
    cmd = r".. method:: FrameBuffer."
    rect = r"rect(x, y, w, h, c)"
    shed.defs_with_common_description(
        cmd=cmd,
        old2new={
            "hline(x, y, w, c)": "def hline(self, x: int, y: int, w: int, c: int, /) -> None",
            "vline(x, y, h, c)": "def vline(self, x: int, y: int, h: int, c: int, /) -> None",
            "line(x1, y1, x2, y2, c)": "def line(self, x1: int, y1: int, x2: int, y2: int, c: int, /) -> None",
        },
        end=cmd + rect,
    )
    shed.defs_with_common_description(
        cmd=cmd,
        old2new={
            rect: "def rect(self, x: int, y: int, w: int, h: int, c: int, /) -> None",
            "fill_rect(x, y, w, h, c)": "def fill_rect(self, x: int, y: int, w: int, h: int, c: int, /) -> None",
        },
        end="Drawing text",
    )
    shed.def_(
        old=r".. method:: FrameBuffer.text(s, x, y[, c])",
        new="def text(self, s: str, x: int, y: int, c: int = 1, /) -> None",
    )
    shed.def_(
        old=r".. method:: FrameBuffer.scroll(xstep, ystep)",
        new="def scroll(self, xstep: int, ystep: int, /) -> None",
    )
    shed.def_(
        old=r".. method:: FrameBuffer.blit(fbuf, x, y, key=-1, palette=None)",
        new="""
def blit(self, fbuf: FrameBuffer, x: int, y: int, key: int = -1, pallet: FrameBuffer | None = None, /) -> None
""",
    )
    shed.vars(
        old=".. data:: framebuf.MONO_VLSB", class_var=None,
    )
    shed.vars(
        old=".. data:: framebuf.MONO_HLSB", class_var=None,
    )
    shed.vars(
        old=".. data:: framebuf.MONO_HMSB", class_var=None,
    )
    shed.vars(
        old=".. data:: framebuf.RGB565", class_var=None,
    )
    shed.vars(
        old=".. data:: framebuf.GS2_HMSB", class_var=None,
    )
    shed.vars(
        old=".. data:: framebuf.GS4_HMSB", class_var=None,
    )
    shed.vars(
        old=".. data:: framebuf.GS8", class_var=None, end=None,
    )
    shed.write()
