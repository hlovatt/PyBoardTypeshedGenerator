"""
Generate `pyi` from corresponding `rst` docs.
"""

import rst
from rst2pyi import RST2PyI

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = "7.5.3"  # Version set by https://github.com/hlovatt/tag2ver


def bluetooth(shed: RST2PyI) -> None:
    shed.module(
        name="bluetooth",
        old="Low-level Bluetooth radio functionality",
        post_doc=f"""
from typing import overload, Any, Callable, Final

from uio import AnyReadableBuf, AnyWritableBuf
""",
        end="class BLE",
    )
    shed.class_(
        pre_str="# noinspection SpellCheckingInspection", name="BLE", end="Constructor",
    )
    shed.def_(
        old=r".. class:: BLE()", new="def __init__(self)", end="Configuration",
    )
    shed.def_(
        old=r".. method:: BLE.active([active], /)",
        new=["def active(self) -> bool", "def active(self, active: bool, /) -> None"],
    )
    shed.defs_with_common_description(
        cmd=r".. method:: BLE.",  # Needs `.` at end!
        old2new={
            r"config('param', /)": """
@overload
def config(self, param: str, /) -> Any
""",
            r"config(*, param=value, ...)": """
@overload
def config(self, **kwargs) -> None
""",
        },
        end="Event Handling",
    )
    shed.def_(
        old=r".. method:: BLE.irq(handler, /)",
        new="def irq(self, handler: Callable[[int, tuple[memoryview, ...]], Any], /) -> None",
        end="Broadcaster Role (Advertiser)",
    )
    shed.consume_minuses_underline_line(and_preceding_lines=True)
    extra_docs = shed.extra_docs()
    shed.def_(
        old=r".. method:: BLE.gap_advertise(interval_us, adv_data=None, *, resp_data=None, connectable=True)",
        new="""
def gap_advertise(
   self, 
   interval_us: int, 
   adv_data: AnyReadableBuf | None = None, 
   /, 
   *,
   resp_data: AnyReadableBuf | None = None, 
   connectable: bool = True
) -> None
""",
        extra_docs=extra_docs,
        end="Observer Role (Scanner)",
    )
    shed.consume_minuses_underline_line(and_preceding_lines=True)
    extra_docs = shed.extra_docs()
    shed.def_(
        old=r".. method:: BLE.gap_scan(duration_ms, interval_us=1280000, window_us=11250, active=False, /)",
        new="""
def gap_scan(
   self, 
   duration_ms: int,
   interval_us: int = 1280000, 
   window_us: int = 11250, 
   active: bool = False,
   /,
) -> None
""",
        extra_docs=extra_docs,
        end="Central Role",
    )
    extra_docs = shed.extra_docs()
    shed.def_(
        old=r".. method:: BLE.gap_connect(addr_type, addr, scan_duration_ms=2000, min_conn_interval_us=None, max_conn_interval_us=None, /)",
        new="""
def gap_connect(
   self, 
   addr_type: int,
   addr: bytes, 
   scan_duration_ms: int = 2000, 
   min_conn_interval_us: int | None = None, 
   max_conn_interval_us: int | None = None,
   /,
) -> None
""",
        extra_docs=extra_docs,
        end="Peripheral Role",
    )
    extra_docs += shed.extra_docs(
        end="Central & Peripheral Roles"
    )  # Note append, disconnect has two roles.
    shed.consume_minuses_underline_line(and_preceding_lines=True)
    shed.def_(
        old=r".. method:: BLE.gap_disconnect(conn_handle, /)",
        new="def gap_disconnect(self, conn_handle: memoryview, /) -> bool",
        extra_docs=extra_docs,
        end="GATT Server",
    )
    extra_docs = shed.extra_docs()
    shed.pyi.classes[-1].defs += [
        "   _Flag: Final = int",
        '   _Descriptor: Final = tuple["UUID", _Flag]',
        '   _Characteristic: Final = tuple["UUID", _Flag] | tuple["UUID", _Flag, tuple[_Descriptor, ...]]',
        '   _Service: Final = tuple["UUID", tuple[_Characteristic, ...]]',
    ]
    shed.def_(
        old=r".. method:: BLE.gatts_register_services(services_definition, /)",
        new="""
def gatts_register_services(
   self, 
   services_definition: tuple[_Service, ...], 
   /
) -> tuple[tuple[memoryview, ...], ...]
""",
        extra_docs=extra_docs,
    )
    shed.def_(
        old=r".. method:: BLE.gatts_read(value_handle, /)",
        new="def gatts_read(self, value_handle: memoryview, /) -> bytes",
        extra_docs=extra_docs,
    )
    shed.def_(
        old=r".. method:: BLE.gatts_write(value_handle, data, send_update=False, /)",
        new="def gatts_write(self, value_handle: memoryview, data: bytes, send_update: bool = False, /) -> None",
        extra_docs=extra_docs,
    )
    shed.def_(
        old=r".. method:: BLE.gatts_notify(conn_handle, value_handle, data=None, /)",
        new="def gatts_notify(self, value_handle: memoryview, data: bytes, /) -> None",
        extra_docs=extra_docs,
    )
    shed.def_(
        old=r".. method:: BLE.gatts_indicate(conn_handle, value_handle, /)",
        new="def gatts_indicate(self, conn_handle: memoryview, value_handle: memoryview, /) -> None",
        extra_docs=extra_docs,
    )
    shed.def_(
        old=r".. method:: BLE.gatts_set_buffer(value_handle, len, append=False, /)",
        new="def gatts_set_buffer(self, conn_handle: memoryview, len: int, append: bool = False, /) -> None",
        end="GATT Client",
        extra_docs=extra_docs,
    )
    extra_docs = shed.extra_docs()
    shed.def_(
        old=r".. method:: BLE.gattc_discover_services(conn_handle, uuid=None, /)",
        new="def gattc_discover_services(self, conn_handle: memoryview, uuid: UUID | None = None, /) -> None",
        extra_docs=extra_docs,
    )
    shed.def_(
        old=r".. method:: BLE.gattc_discover_characteristics(conn_handle, start_handle, end_handle, uuid=None, /)",
        new="""
def gattc_discover_characteristics(
   self, 
   conn_handle: memoryview, 
   start_handle: int, 
   end_handle: int, 
   uuid: UUID | None = None, 
   /
) -> None
""",
        extra_docs=extra_docs,
    )
    shed.def_(
        old=r".. method:: BLE.gattc_discover_descriptors(conn_handle, start_handle, end_handle, /)",
        new="""
def gattc_discover_descriptors(
   self, 
   conn_handle: memoryview, 
   start_handle: int, 
   end_handle: int, 
   /
) -> None
""",
        extra_docs=extra_docs,
    )
    shed.def_(
        old=r".. method:: BLE.gattc_read(conn_handle, value_handle, /)",
        new="def gattc_read(self, conn_handle: memoryview, value_handle: memoryview, /) -> None",
        extra_docs=extra_docs,
    )
    shed.def_(
        old=r".. method:: BLE.gattc_write(conn_handle, value_handle, data, mode=0, /)",
        new="""
def gattc_write(
   self, 
   conn_handle: memoryview, 
   value_handle: memoryview, 
   data: bytes, 
   mode: int = 0,
   /
) -> None
""",
        extra_docs=extra_docs,
    )
    shed.def_(
        old=r".. method:: BLE.gattc_exchange_mtu(conn_handle, /)",
        new="def gattc_exchange_mtu(self, conn_handle: memoryview, /) -> None",
        extra_docs=extra_docs,
        end="L2CAP connection-oriented-channels",
    )
    extra_docs = shed.extra_docs()
    shed.def_(
        old=r".. method:: BLE.l2cap_listen(psm, mtu, /)",
        new="def l2cap_listen(self, psm: memoryview, mtu: memoryview, /) -> None",
        extra_docs=extra_docs,
    )
    shed.def_(
        old=r".. method:: BLE.l2cap_connect(conn_handle, psm, mtu, /)",
        new="def l2cap_connect(self, conn_handle: memoryview, psm: memoryview, mtu: memoryview, /) -> None",
        extra_docs=extra_docs,
    )
    shed.def_(
        old=r".. method:: BLE.l2cap_disconnect(conn_handle, cid, /)",
        new="def l2cap_disconnect(self, conn_handle: memoryview, cid: memoryview, /) -> None",
        extra_docs=extra_docs,
    )
    shed.def_(
        old=r".. method:: BLE.l2cap_send(conn_handle, cid, buf, /)",
        new="def l2cap_send(self, conn_handle: memoryview, cid: memoryview, /) -> None",
        extra_docs=extra_docs,
    )
    shed.def_(
        old=r".. method:: BLE.l2cap_recvinto(conn_handle, cid, buf, /)",
        new="""
def l2cap_recvinto(
   self, 
   conn_handle: memoryview, 
   cid: memoryview, 
   buf: AnyWritableBuf | None, 
   /
) -> int
""",
        extra_docs=extra_docs,
        end="Pairing and bonding",
    )
    extra_docs = shed.extra_docs()
    shed.def_(
        old=r".. method:: BLE.gap_pair(conn_handle, /)",
        new="def gap_pair(self, conn_handle: memoryview, /) -> None",
        extra_docs=extra_docs,
    )
    shed.def_(
        old=r".. method:: BLE.gap_passkey(conn_handle, action, passkey, /)",
        new="def gap_passkey(self, conn_handle: memoryview, action: int, passkey: int, /) -> None",
        extra_docs=extra_docs,
        end="class UUID",
    )
    shed.class_(
        name="UUID", end="Constructor",
    )
    shed.def_(
        old=r".. class:: UUID(value, /)", new="def __init__(self, value: int | str, /)",
    )
    shed.write(u_also=True)
