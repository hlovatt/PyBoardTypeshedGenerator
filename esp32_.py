"""
Generate `pyi` from corresponding `rst` docs.
"""
from typing import Final

import rst
from rst2pyi import RST2PyI

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = "7.5.2"  # Version set by https://github.com/hlovatt/tag2ver


def esp32(shed: RST2PyI) -> None:
    shed.module(
        name="esp32",
        old="functionality specific to the ESP32",
        post_doc="""
from typing import Final, List, Tuple, overload, ClassVar

from machine import Pin
from uio import AnyReadableBuf
from uos import AbstractBlockDev
""",
        end="Functions",
    )

    shed.def_(
        old=r".. function:: wake_on_touch(wake)",
        new="def wake_on_touch(wake: bool, /) -> None",
        indent=0,
    )
    shed.def_(
        old=r".. function:: wake_on_ext0(pin, level)",
        new="def wake_on_ext0(pin: Pin | None, level: int, /) -> None",
        indent=0,
    )
    shed.def_(
        old=r".. function:: wake_on_ext1(pins, level)",
        new="def wake_on_ext1(pins: List[Pin] | Tuple[Pin, ...] | None, level: int, /) -> None",
        indent=0,
    )
    shed.def_(
        old=r".. function:: raw_temperature()",
        new="def raw_temperature() -> int",
        indent=0,
    )
    shed.def_(
        old=r".. function:: hall_sensor()", new="def hall_sensor() -> int", indent=0,
    )
    partitions: Final = "Flash partitions"
    shed.def_(
        old=r".. function:: idf_heap_info(capabilities)",
        new="def idf_heap_info(capabilities: int) -> List[Tuple[int, int, int, int]]",
        indent=0,
        end=partitions,
    )

    shed.consume_minuses_underline_line(and_preceding_lines=True)
    partition_init: Final = r".. class:: Partition(id)"
    partition_doc: Final = shed.extra_docs(end=partition_init)
    shed.class_(
        name="Partition(AbstractBlockDev)",
        extra_docs=partition_doc,
        end=partition_init,
    )
    shed.def_(
        old=partition_init, new="def __init__(self, id: str | int, /)",
    )
    shed.def_(
        old=r".. classmethod:: Partition.find(type=TYPE_APP, subtype=0xff, label=None)",
        new="""
@staticmethod
def find(type: int = TYPE_APP, subtype: int = 0xff, label: str | None = None, /) -> List["Partition"]
""",
    )
    shed.def_(
        old=r".. method:: Partition.info()",
        new="def info(self) -> (int, int, int, int, str, bool)",
    )
    shed.consume_containing_line(
        r"Partition.readblocks(block_num, buf)", and_preceding_lines=True
    )
    shed.consume_containing_line(
        r"Partition.readblocks(block_num, buf, offset)", and_preceding_lines=True
    )
    shed.consume_containing_line(
        r"Partition.writeblocks(block_num, buf)", and_preceding_lines=True
    )
    shed.consume_containing_line(
        r"Partition.writeblocks(block_num, buf, offset)", and_preceding_lines=True
    )
    shed.consume_containing_line(r"Partition.ioctl(cmd, arg)", and_preceding_lines=True)
    set_boot: Final = r".. method:: Partition.set_boot()"
    shed.consume_up_to_but_excl_end_line(end=set_boot)
    shed.def_(
        old=set_boot, new="def set_boot(self) -> None",
    )
    shed.def_(
        old=r".. method:: Partition.get_next_update()",
        new='def get_next_update(self) -> "Partition"',
    )
    shed.def_(
        old=r".. classmethod:: Partition.mark_app_valid_cancel_rollback()",
        new="""
@staticmethod
def mark_app_valid_cancel_rollback() -> None
""",
        end="Constants",
    )
    shed.consume_tildes_underline_line(and_preceding_lines=True)
    shed.vars(old=[".. data:: Partition.BOOT", "Partition.RUNNING"])
    shed.vars(old=[".. data:: Partition.TYPE_APP", "Partition.TYPE_DATA"])
    shed.vars(
        old=[".. data:: HEAP_DATA", "HEAP_EXEC"], class_var=None,
    )

    shed.consume_minuses_underline_line(and_preceding_lines=True)
    shed.consume_blank_line()
    rmt_init: Final = r".. class:: RMT(channel, *, pin=None, clock_div=8, idle_level=False, tx_carrier=None)"
    rmt_doc: Final = shed.extra_docs(end=rmt_init)
    shed.class_(name=r"RMT", extra_docs=rmt_doc, end=rmt_init)
    shed.def_(
        old=rmt_init,
        new="""
def __init__(
   self, 
   channel: int, 
   /,
   *, 
   pin: Pin | None = None, 
   clock_div: int = 8, 
   idle_level: bool = False, 
   tx_carrier: Tuple[int, int, bool] | None = None
)
""",
    )
    shed.def_(
        old=r".. method:: RMT.source_freq()", new="def source_freq(self) -> int",
    )
    shed.def_(
        old=r".. method:: RMT.clock_div()", new="def clock_div(self) -> int",
    )
    shed.def_(
        old=r".. method:: RMT.wait_done(*, timeout=0)",
        new="def wait_done(self, *, timeout: int = 0) -> bool",
    )
    shed.def_(
        old=r".. method:: RMT.loop(enable_loop)",
        new="def loop(self, enable_loop: bool, /) -> None",
    )
    ulp_doc: Final = "Ultra-Low-Power co-processor"
    shed.def_(
        old=r".. method:: RMT.write_pulses(duration, data=True)",
        new=[
            "def write_pulses(self, duration: List[int] | Tuple[int, ...], data: bool = True, /) -> None",
            "def write_pulses(self, duration: int, data: List[bool] | Tuple[bool, ...], /) -> None",
            """
def write_pulses(
   self, 
   duration: List[int] | Tuple[int, ...], 
   data: List[bool] | Tuple[bool, ...], 
   /,
) -> None
""",
        ],
        end=ulp_doc,
    )

    shed.consume_containing_line(ulp_doc)
    shed.consume_minuses_underline_line()
    ulp_init: Final = r".. class:: ULP()"
    shed.class_(
        name="ULP",
        extra_docs=[
            "   This class provides access to the Ultra-Low-Power co-processor."
        ],
        end=ulp_init,
    )
    shed.def_(
        old=ulp_init, new="def __init__(self)",
    )
    shed.def_(
        old=r".. method:: ULP.set_wakeup_period(period_index, period_us)",
        new="def set_wakeup_period(self, period_index: int, period_us: int, /) -> None",
    )
    shed.def_(
        old=r".. method:: ULP.load_binary(load_addr, program_binary)",
        new="def load_binary(self, load_addr: int, program_binary: AnyReadableBuf, /) -> None",
    )
    shed.def_(
        old=r".. method:: ULP.run(entry_point)",
        new="def run(self, entry_point: int, /) -> None",
    )

    nvs_doc: Final = "Non-Volatile Storage"
    shed.vars(
        old=[".. data:: esp32.WAKEUP_ALL_LOW", "esp32.WAKEUP_ANY_HIGH",],
        class_var=None,
        end=nvs_doc,
    )

    shed.consume_minuses_underline_line(and_preceding_lines=True)
    nvs_init: Final = r".. class:: NVS(namespace)"
    shed.class_(name="NVS", end=nvs_init)
    shed.def_(old=nvs_init, new="def __init__(self, namespace: str, /)")
    shed.def_(
        old=r".. method:: NVS.set_i32(key, value)",
        new="def set_i32(self, key: str, value: int, /) -> None",
    )
    shed.def_(
        old=r".. method:: NVS.get_i32(key)",
        new="def get_i32(self, key: str, /) -> int",
    )
    shed.def_(
        old=r".. method:: NVS.set_blob(key, value)",
        new="def set_blob(self, key: str, value: AnyReadableBuf, /) -> None",
    )
    shed.def_(
        old=r".. method:: NVS.get_blob(key, buffer)",
        new="def get_blob(self, key: str, buffer: bytearray, /) -> int",
    )
    shed.def_(
        old=r".. method:: NVS.erase_key(key)",
        new="def erase_key(self, key: str, /) -> None",
    )
    shed.def_(
        old=r".. method:: NVS.commit()", new="def commit(self) -> None",
    )

    shed.write()
