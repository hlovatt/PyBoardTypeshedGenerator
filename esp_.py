"""
Generate `pyi` from corresponding `rst` docs.
"""
from typing import Final

import rst
from rst2pyi import RST2PyI

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = "7.4.0"  # Version set by https://github.com/hlovatt/tag2ver


def esp(shed: RST2PyI) -> None:
    shed.module(
        name="esp",
        old="functions related to the ESP8266 and ESP32",
        post_doc='''
from typing import Final, overload

from uio import AnyWritableBuf, AnyReadableBuf

SLEEP_NONE: Final[int] = ...
"""All functions enabled."""

SLEEP_MODEM: Final[int] = ...
"""Modem sleep, shuts down the WiFi Modem circuit."""

SLEEP_LIGHT: Final[int] = ...
"""Light sleep, shuts down the WiFi Modem circuit."""
''',
        end="Functions",
    )

    shed.def_(
        old=r".. function:: sleep_type([sleep_type])",
        pre_str="# noinspection PyShadowingNames",
        new=["def sleep_type(sleep_type: int, /) -> None", "def sleep_type() -> int",],
        indent=0,
    )
    shed.def_(
        old=r".. function:: deepsleep(time_us=0, /)",
        new="def deepsleep(time_us: int = 0, /) -> None",
        indent=0,
    )
    shed.def_(
        old=r".. function:: flash_id()", new="def flash_id() -> int", indent=0,
    )
    shed.def_(
        old=r".. function:: flash_size()", new="def flash_size() -> int", indent=0,
    )
    shed.def_(
        old=r".. function:: flash_user_start()",
        new="def flash_user_start() -> int",
        indent=0,
    )
    shed.def_(
        old=r".. function:: flash_read(byte_offset, length_or_buffer)",
        new=[
            "def flash_read(byte_offset: int, length_or_buffer: int, /) -> bytes",
            "def flash_read(byte_offset: int, length_or_buffer: AnyWritableBuf, /) -> None",
        ],
        extra_docs=[
            "   Reads bytes from the flash memory starting at the given byte offset.",
            "   If length is specified: reads the given length of bytes and returns them as ``bytes``.",
            "   If a buffer is given: reads the buf length of bytes and writes them into the buffer.",
            "   Note: esp32 doesn't support passing a length, just a buffer.",
        ],
        indent=0,
    )
    shed.def_(
        old=r".. function:: flash_write(byte_offset, bytes)",
        new="def flash_write(byte_offset: int, bytes: AnyReadableBuf, /) -> None",
        extra_docs=[
            "   Writes given bytes buffer to the flash memory starting at the given byte offset.",
        ],
        indent=0,
    )
    shed.def_(
        old=r".. function:: flash_erase(sector_no)",
        new="def flash_erase(sector_no: int, /) -> None",
        extra_docs=["   Erases the given *sector* of flash memory.",],
        indent=0,
    )
    shed.def_(
        old=r".. function:: set_native_code_location(start, length)",
        new=[
            "def set_native_code_location(start: None, length: None, /) -> None",
            "def set_native_code_location(start: int, length: int, /) -> None",
        ],
        indent=0,
    )

    shed.write()
