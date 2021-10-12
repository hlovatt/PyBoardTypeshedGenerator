"""
Generate `pyi` from corresponding `rst` docs.
"""

import rst
from rst2pyi import RST2PyI

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = "7.0.0"  # Version set by https://github.com/hlovatt/tag2ver


def lcd160cr(shed: RST2PyI) -> None:
    shed.module(
        name=r"lcd160cr",
        old="control of LCD160CR display",
        post_doc=f"""
from typing import overload, Any, Final

from pyb import Pin, I2C, SPI
from uio import AnyReadableBuf, AnyWritableBuf
""",
        end=r"..",
    )
    shed.pyi.doc.extend(shed.extra_notes(end="class LCD160CR",))
    shed.consume_minuses_underline_line(and_preceding_lines=True)
    shed.consume_blank_line()
    shed.class_(name="LCD160CR", end="Constructors")
    shed.def_(
        old=r".. class:: LCD160CR(connect=None, *, pwr=None, i2c=None, spi=None, i2c_addr=98)",
        new=[
            "def __init__(self, connect: str, /)",
            "def __init__(self, *, pwr: Pin, i2c: I2C, spi: SPI, i2c_addr: int = 98)",
        ],
    )
    shed.def_(
        old=".. staticmethod:: LCD160CR.rgb(r, g, b)",
        new="""
@staticmethod
def rgb(r: int, g: int, b: int, /) -> int
""",
    )
    shed.def_(
        old=".. staticmethod:: LCD160CR.clip_line(data, w, h):",
        new="""
@staticmethod
def clip_line(data: Any, w: int, h: int, /) -> int
""",
    )
    shed.vars(
        old=[".. data:: LCD160CR.w", ".. data:: LCD160CR.h"],
        class_var=False,
        end="Setup commands",
    )
    shed.def_(
        old=".. method:: LCD160CR.set_power(on)",
        new="def set_power(self, on: bool, /) -> None",
    )
    shed.def_(
        old=".. method:: LCD160CR.set_orient(orient)",
        new="def set_orient(self, orient: str, /) -> None",
    )
    shed.def_(
        old=".. method:: LCD160CR.set_brightness(value)",
        new="def set_brightness(self, value: int, /) -> None",
    )
    shed.def_(
        old=".. method:: LCD160CR.set_i2c_addr(addr)",
        new="def set_i2c_addr(self, addr: int, /) -> None",
    )
    shed.def_(
        old=".. method:: LCD160CR.set_uart_baudrate(baudrate)",
        new="def set_uart_baudrate(self, baudrate: int, /) -> None",
    )
    shed.def_(
        old=".. method:: LCD160CR.set_startup_deco(value)",
        new="def set_startup_deco(self, value: bool | str, /) -> None",
    )
    shed.def_(
        old=".. method:: LCD160CR.save_to_flash()",
        new="def save_to_flash(self) -> None",
    )
    shed.def_(
        old=".. method:: LCD160CR.set_pixel(x, y, c)",
        new="def set_pixel(self, x: int, y: int, c: int, /) -> None",
    )
    shed.def_(
        old=".. method:: LCD160CR.get_pixel(x, y)",
        new="def get_pixel(self, x: int, y: int, /) -> int",
    )
    shed.def_(
        old=".. method:: LCD160CR.get_line(x, y, buf)",
        new="def get_line(self, x: int, y: int, buf: AnyWritableBuf, /) -> None",
    )
    shed.def_(
        old=".. method:: LCD160CR.screen_dump(buf, x=0, y=0, w=None, h=None)",
        new="""
def screen_dump(
   self, 
   buf: AnyWritableBuf, 
   x: int = 0, 
   y: int = 0, 
   w: int | None = None, 
   h: int | None = None, 
   /
) -> None
""",
    )
    shed.def_(
        old=".. method:: LCD160CR.screen_load(buf)",
        new="def screen_load(self, buf: AnyReadableBuf, /) -> None",
    )
    shed.def_(
        old=".. method:: LCD160CR.set_pos(x, y)",
        new="def set_pos(self, x: int, y: int, /) -> None",
    )
    shed.def_(
        old=".. method:: LCD160CR.set_text_color(fg, bg)",
        new="def set_text_color(self, fg: int, bg: int, /) -> None",
    )
    shed.def_(
        old=".. method:: LCD160CR.set_font(font, scale=0, bold=0, trans=0, scroll=0)",
        new="def set_font(self, font: int, scale: int = 0, bold: int = 0, trans: int = 0, scroll: int = 0, /) -> None",
    )
    shed.def_(
        old=".. method:: LCD160CR.write(s)", new="def write(self, s: str, /) -> None",
    )
    shed.def_(
        old=".. method:: LCD160CR.set_pen(line, fill)",
        new="def set_pen(self, line: int, fill: int, /) -> None",
    )
    shed.def_(
        old=".. method:: LCD160CR.erase()", new="def erase(self) -> None",
    )
    shed.def_(
        old=".. method:: LCD160CR.dot(x, y)",
        new="def dot(self, x: int, y: int, /) -> None",
    )
    line_def = ".. method:: LCD160CR.line(x1, y1, x2, y2)"
    shed.defs_with_common_description(
        cmd=".. method:: LCD160CR.",  # Needs `.` at end!
        old2new={
            "rect(x, y, w, h)": "def rect(self, x: int, y: int, w: int, h: int, /) -> None",
            "rect_outline(x, y, w, h)": "def rect_outline(self, x: int, y: int, w: int, h: int, /) -> None",
            "rect_interior(x, y, w, h)": "def rect_interior(self, x: int, y: int, w: int, h: int, /) -> None",
        },
        end=line_def,
    )
    shed.def_(
        old=line_def,
        new="def line(self, x1: int, y1: int, x2: int, y2: int, /) -> None",
    )
    poly_dot_def = ".. method:: LCD160CR.poly_dot(data)"
    shed.defs_with_common_description(
        cmd=".. method:: LCD160CR.",  # Needs `.` at end!
        old2new={
            "dot_no_clip(x, y)": "def dot_no_clip(self, x: int, y: int, /) -> None",
            "rect_no_clip(x, y, w, h)": "def rect_no_clip(self, x: int, y: int, w: int, h: int, /) -> None",
            "rect_outline_no_clip(x, y, w, h)": "def rect_outline_no_clip(self, x: int, y: int, w: int, h: int, /) -> None",
            "rect_interior_no_clip(x, y, w, h)": "def rect_interior_no_clip(self, x: int, y: int, w: int, h: int, /) -> None",
            "line_no_clip(x1, y1, x2, y2)": "def line_no_clip(self, x1: int, y1: int, x2: int, y2: int, /) -> None",
        },
        end=poly_dot_def,
    )
    shed.def_(
        old=poly_dot_def, new="def poly_dot(self, data: AnyReadableBuf, /) -> None",
    )
    shed.def_(
        old=".. method:: LCD160CR.poly_line(data)",
        new="def poly_line(self, data: AnyReadableBuf, /) -> None",
    )
    shed.def_(
        old=".. method:: LCD160CR.touch_config(calib=False, save=False, irq=None)",
        new="def touch_config(self, calib: bool = False, save: bool = False, irq: bool | None = None, /) -> None",
    )
    shed.def_(
        old=".. method:: LCD160CR.is_touched()", new="def is_touched(self) -> bool",
    )
    shed.def_(
        old=".. method:: LCD160CR.get_touch()",
        new="def get_touch(self) -> tuple[int, int, int]",
    )
    shed.def_(
        old=".. method:: LCD160CR.set_spi_win(x, y, w, h)",
        new="def set_spi_win(self, x: int, y: int, w: int, h: int, /) -> None",
    )
    shed.def_(
        old=".. method:: LCD160CR.fast_spi(flush=True)",
        new="def fast_spi(self, flush: bool = True, /) -> SPI",
    )
    shed.def_(
        old=".. method:: LCD160CR.show_framebuf(buf)",
        new="def show_framebuf(self, buf: AnyReadableBuf, /) -> None",
    )
    shed.def_(
        old=".. method:: LCD160CR.set_scroll(on)",
        new="def set_scroll(self, on: bool, /) -> None",
    )
    shed.def_(
        old=".. method:: LCD160CR.set_scroll_win(win, x=-1, y=0, w=0, h=0, vec=0, pat=0, fill=0x07e0, color=0)",
        new="""
def set_scroll_win(
   self, 
   win: int, 
   x: int = -1, 
   y: int = 0, 
   w: int = 0, 
   h: int = 0, 
   vec: int = 0, 
   pat: int = 0, 
   fill: int = 0x07e0, 
   color: int = 0, 
   /
) -> None""",
    )
    shed.def_(
        old=".. method:: LCD160CR.set_scroll_win_param(win, param, value)",
        new="def set_scroll_win_param(self, win: int, param: int, value: int, /) -> None",
    )
    shed.def_(
        old=".. method:: LCD160CR.set_scroll_buf(s)",
        new="def set_scroll_buf(self, s: str, /) -> None",
    )
    shed.def_(
        old=".. method:: LCD160CR.jpeg(buf)",
        new="def jpeg(self, buf: AnyReadableBuf, /) -> None",
    )
    feed_wdt_def = ".. method:: LCD160CR.feed_wdt()"
    shed.defs_with_common_description(
        cmd=".. method:: LCD160CR.",  # Needs `.` at end!
        old2new={
            "jpeg_start(total_len)": "def jpeg_start(self, total_len: int, /) -> None",
            "jpeg_data(buf)": "def jpeg_data(self, buf: AnyReadableBuf, /) -> None",
        },
        end=feed_wdt_def,
    )
    shed.def_(
        old=feed_wdt_def, new="def feed_wdt(self) -> None",
    )
    shed.def_(
        old=".. method:: LCD160CR.reset()", new="def reset(self) -> None",
    )
    shed.vars(
        old=[
            ".. data:: lcd160cr.PORTRAIT",
            "lcd160cr.LANDSCAPE",
            "lcd160cr.PORTRAIT_UPSIDEDOWN",
            "lcd160cr.LANDSCAPE_UPSIDEDOWN",
        ],
        type_="str",
        class_var=None,
    )
    shed.vars(
        old=[
            ".. data:: lcd160cr.STARTUP_DECO_NONE",
            "lcd160cr.STARTUP_DECO_MLOGO",
            "lcd160cr.STARTUP_DECO_INFO",
        ],
        class_var=None,
        end=None,
    )
    shed.write()
