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


def machine(shed: RST2PyI) -> None:
    _machine(shed)
    nxt = _pin(shed)
    nxt = _signal(nxt, shed)
    nxt = _adc(nxt, shed)
    nxt = _pwm(nxt, shed)
    nxt = _uart(nxt, shed)
    nxt = _spi(nxt, shed)
    nxt = _i2c(nxt, shed)
    nxt = _i2s(nxt, shed)
    nxt = _rtc(nxt, shed)
    nxt = _timer(nxt, shed)
    nxt = _wdt(nxt, shed)
    nxt = _sd(nxt, shed)
    _sd_card(nxt, shed)

    shed.write()


def _i2s(this: str, shed: RST2PyI) -> str:
    shed.class_from_file(
        old=this, end="Constructors",
    )
    shed.def_(
        old=r".. class:: I2S(id, *, sck, ws, sd, mode, bits, format, rate, ibuf)",
        new="""
def __init__(
   self, 
   id: int, 
   /,
   *, 
   sck: Pin, 
   ws: Pin, 
   sd: Pin,
   mode: int,
   bits: int,
   format: int,
   rate: int,
   ibuf: int,
)
""",
        end="Methods",
    )

    shed.def_(
        old=r".. method:: I2S.init(sck, ...)",
        new="""
def init(
   self, 
   *, 
   sck: Pin, 
   ws: Pin, 
   sd: Pin, 
   mode: int, 
   bits: int, 
   format: int, 
   rate: int, 
   ibuf: int
) -> None
""",
    )
    shed.def_(
        old=r".. method:: I2S.deinit()", new="def deinit(self) -> None",
    )
    shed.def_(
        old=r".. method::  I2S.readinto(buf)",
        new="def readinto(self, buf: AnyWritableBuf, /,) -> int",
    )
    shed.def_(
        old=r".. method::  I2S.write(buf)",
        new="def write(self, buf: AnyReadableBuf, /,) -> int",
    )
    shed.def_(
        old=r".. method::  I2S.irq(handler)",
        new="def irq(self, handler: Callable[[], None], /,) -> None",
    )

    shed.def_(
        old=r".. staticmethod::  I2S.shift(*, buf, bits, shift)",
        new="""
@staticmethod
def shift(buf: AnyWritableBuf, bits: int, shift: int, /,) -> None
""",
    )

    shed.vars(old=r".. data:: I2S.RX",)
    shed.vars(old=r".. data:: I2S.TX",)
    shed.vars(old=r".. data:: I2S.STEREO",)
    nxt = "machine.RTC.rst"
    shed.vars(old=r".. data:: I2S.MONO", end=nxt)
    return nxt


def _pwm(this: str, shed: RST2PyI) -> str:
    shed.class_from_file(
        pre_str="# noinspection PyShadowingNames", old=this, end="Constructors",
    )
    shed.def_(
        old=r".. class:: PWM(dest, \*, freq, duty_u16, duty_ns)",
        new="""
def __init__(
   self, 
   dest: Pin | int, 
   /,
   *, 
   freq: int = ..., 
   duty_u16: int = ..., 
   duty_ns: int = ...,
)
""",
        end="Methods",
    )
    shed.def_(
        old=r".. method:: PWM.init(\*, freq, duty_u16, duty_ns)",
        new="def init(self, *, freq: int = ..., duty_u16: int = ..., duty_ns: int = ...) -> None",
    )
    shed.def_(
        old=r".. method:: PWM.deinit()", new="def deinit(self) -> None",
    )
    shed.def_(
        old=r".. method:: PWM.freq([value])",
        new=["def freq(self) -> int", "def freq(self, value: int, /,) -> None"],
    )
    shed.def_(
        old=r".. method:: PWM.duty_u16([value])",
        new=["def duty_u16(self) -> int", "def duty_u16(self, value: int, /,) -> None"],
    )
    shed.def_(
        old=r".. method:: PWM.duty_ns([value])",
        new=["def duty_ns(self) -> int", "def duty_ns(self, value: int, /,) -> None"],
        end="Limitations of PWM",
    )
    nxt = "machine.UART.rst"
    extra_docs = shed.extra_docs(end=nxt)
    shed.pyi.classes[-1].doc.extend(extra_docs)
    return nxt


def _sd_card(this: str, shed: RST2PyI) -> None:
    con: Final = """
.. class:: SDCard(slot=1, width=1, cd=None, wp=None, sck=None, miso=None, mosi=None, cs=None, freq=20000000)
""".strip()
    shed.class_from_file(
        pre_str="# noinspection PyShadowingNames",
        old=this,
        super_class="AbstractBlockDev",
        end=con,
    )
    shed.def_(
        old=con,
        new="""
def __init__(
   self, 
   slot: int = 1, 
   width: int = 1, 
   cd: int | str | Pin | None = None, 
   wp: int | str | Pin | None = None, 
   sck: int | str | Pin | None = None, 
   miso: int | str | Pin | None = None, 
   mosi: int | str | Pin | None = None, 
   cs: int | str | Pin | None = None, 
   freq: int = 20000000,
   /,
)
""",
        end="Implementation-specific details",
    )
    shed.pyi.classes[-1].doc += shed.extra_docs()


def _sd(this: str, shed: RST2PyI) -> str:
    shed.class_from_file(old=this,)
    shed.def_(
        old=r".. class:: SD(id,... )",
        new="""
def __init__(
   self, 
   id: int = 0, 
   pins: tuple[str, str, str] | tuple[Pin, Pin, Pin] = ("GP10", "GP11", "GP15"),
   /,
)
""",
    )
    shed.def_(
        old=r".. method:: SD.init(id=0, pins=('GP10', 'GP11', 'GP15'))",
        new="""
def init(
   self, 
   id: int = 0, 
   pins: tuple[str, str, str] | tuple[Pin, Pin, Pin] = ("GP10", "GP11", "GP15"),
   /,
) -> None
""",
    )
    nxt = "machine.SDCard.rst"
    shed.def_(
        old=r".. method:: SD.deinit()", new="def deinit(self) -> None", end=nxt,
    )
    return nxt


def _wdt(this: str, shed: RST2PyI) -> str:
    shed.class_from_file(old=this,)
    shed.def_(
        old=".. class:: WDT(id=0, timeout=5000)",
        new="def __init__(self, *, id: int = 0, timeout: int = 5000)",
    )
    nxt = "machine.SD.rst"
    shed.def_(
        old=".. method:: wdt.feed()", new="def feed(self) -> None", end=nxt,
    )
    return nxt


def _timer(this: str, shed: RST2PyI) -> str:
    shed.class_from_file(old=this,)
    shed.def_(
        old=r".. class:: Timer(id, /, ...)",
        new=[
            """
def __init__(
   self, 
   id: int, 
   /
)
""",
            """
def __init__(
   self, 
   id: int, 
   /, 
   *, 
   mode: int = PERIODIC, 
   period: int = -1, 
   callback: Callable[[Timer], None] | None = None, 
)
""",
        ],
    )
    shed.def_(
        old=r".. method:: Timer.init(*, mode=Timer.PERIODIC, period=-1, callback=None)",
        new="""
def init(
   self, 
   *, 
   mode: int = PERIODIC, 
   period: int = -1, 
   callback: Callable[[Timer], None] | None = None, 
) -> None
""",
    )
    shed.def_(
        old=r".. method:: Timer.deinit()", new="def deinit(self) -> None",
    )
    nxt = "machine.WDT.rst"
    shed.vars(old=[".. data:: Timer.ONE_SHOT", "Timer.PERIODIC"], end=nxt)
    return nxt


def _rtc(this: str, shed: RST2PyI) -> str:
    disclaimer = [
        "The documentation for RTC is in a poor state; better to experiment and use `dir`!"
    ]
    shed.class_from_file(old=this, extra_docs=disclaimer, end="Constructors")
    shed.def_(
        old=".. class:: RTC(id=0, ...)",
        new=[
            "def __init__(self, id: int = 0, /, *, datetime: tuple[int, int, int])",
            "def __init__(self, id: int = 0, /, *, datetime: tuple[int, int, int, int])",
            "def __init__(self, id: int = 0, /, *, datetime: tuple[int, int, int, int, int])",
            "def __init__(self, id: int = 0, /, *, datetime: tuple[int, int, int, int, int, int])",
            "def __init__(self, id: int = 0, /, *, datetime: tuple[int, int, int, int, int, int, int])",
            "def __init__(self, id: int = 0, /, *, datetime: tuple[int, int, int, int, int, int, int, int])",
        ],
        extra_docs=disclaimer,
        end="Methods",
    )
    shed.def_(
        old=".. method:: RTC.init(datetime)",
        new=[
            "def init(self) -> None",
            "def init(self, datetime: tuple[int, int, int], /) -> None",
            "def init(self, datetime: tuple[int, int, int, int], /) -> None",
            "def init(self, datetime: tuple[int, int, int, int, int], /) -> None",
            "def init(self, datetime: tuple[int, int, int, int, int, int], /) -> None",
            "def init(self, datetime: tuple[int, int, int, int, int, int, int], /) -> None",
            "def init(self, datetime: tuple[int, int, int, int, int, int, int, int], /) -> None",
        ],
        extra_docs=disclaimer,
    )
    shed.def_(
        old=".. method:: RTC.now()",
        new="def now(self) -> tuple[int, int, int, int, int, int, int, int]",
        extra_docs=disclaimer,
    )
    shed.def_(
        old=".. method:: RTC.deinit()",
        new="def deinit(self) -> None",
        extra_docs=disclaimer,
    )
    shed.def_(
        old=".. method:: RTC.alarm(id, time, *, repeat=False)",
        new=[
            "def alarm(self, id: int, time: int, /, *, repeat: bool = False) -> None",
            "def alarm(self, id: int, time: tuple[int, int, int], /) -> None",
            "def alarm(self, id: int, time: tuple[int, int, int, int], /) -> None",
            "def alarm(self, id: int, time: tuple[int, int, int, int, int], /) -> None",
            "def alarm(self, id: int, time: tuple[int, int, int, int, int, int], /) -> None",
            "def alarm(self, id: int, time: tuple[int, int, int, int, int, int, int], /) -> None",
            "def alarm(self, id: int, time: tuple[int, int, int, int, int, int, int, int], /) -> None",
        ],
        extra_docs=disclaimer,
    )
    shed.def_(
        old=".. method:: RTC.alarm_left(alarm_id=0)",
        new="def alarm_left(self, alarm_id: int = 0, /) -> int",
        extra_docs=disclaimer,
    )
    shed.def_(
        old=".. method:: RTC.cancel(alarm_id=0)",
        new="def cancel(self, alarm_id: int = 0, /) -> None",
        extra_docs=disclaimer,
    )
    shed.def_(
        old=".. method:: RTC.irq(*, trigger, handler=None, wake=machine.IDLE)",
        new="""
def irq(
   self, 
   /, 
   *, 
   trigger: int, 
   handler: Callable[[RTC], None] | None = None, 
   wake: int = IDLE
) -> None
""",
    )
    nxt = "machine.Timer.rst"
    shed.vars(
        old=".. data:: RTC.ALARM0", extra_docs=disclaimer, end=nxt,
    )
    return nxt


def _i2c(this: str, shed: RST2PyI) -> str:
    shed.class_from_file(
        pre_str="# noinspection PyShadowingNames", old=this,
    )
    shed.def_(
        old=r".. class:: I2C(id, *, scl, sda, freq=400000)",
        new=[
            "def __init__(self, id: int, /, *, freq: int = 400_000)",
            "def __init__(self, id: int, /, *, scl: Pin, sda: Pin, freq: int = 400_000)",
        ],
    )
    shed.def_(
        old=r".. method:: I2C.init(scl, sda, *, freq=400000)",
        new=[
            "def init(self, *, freq: int = 400_000) -> None",
            "def init(self, *, scl: Pin, sda: Pin, freq: int = 400_000) -> None",
        ],
    )
    shed.def_(
        old=r".. method:: I2C.deinit()", new="def deinit(self) -> None",
    )
    primitive_docs_start = "Primitive I2C operations"
    shed.def_(
        old=r".. method:: I2C.scan()",
        new="def scan(self) -> list[int]",
        end=primitive_docs_start,
    )
    primitive_docs = shed.extra_docs()
    shed.def_(
        old=r".. method:: I2C.start()",
        new="def start(self) -> None",
        extra_docs=primitive_docs,
    )
    shed.def_(
        old=r".. method:: I2C.stop()",
        new="def stop(self) -> None",
        extra_docs=primitive_docs,
    )
    shed.def_(
        old=r".. method:: I2C.readinto(buf, nack=True, /)",
        new="def readinto(self, buf: AnyWritableBuf, nack: bool = True, /) -> None",
        extra_docs=primitive_docs,
    )
    shed.def_(
        old=r".. method:: I2C.write(buf)",
        new="def write(self, buf: AnyReadableBuf, /) -> int",
        extra_docs=primitive_docs,
        end="Standard bus operations",
    )
    standard_docs = shed.extra_docs()
    shed.def_(
        old=r".. method:: I2C.readfrom(addr, nbytes, stop=True, /)",
        new="def readfrom(self, addr: int, nbytes: int, stop: bool = True, /) -> bytes",
        extra_docs=standard_docs,
    )
    shed.def_(
        old=r".. method:: I2C.readfrom_into(addr, buf, stop=True, /)",
        new="def readfrom_into(self, addr: int, buf: AnyWritableBuf, stop: bool = True, /) -> None",
        extra_docs=standard_docs,
    )
    shed.def_(
        old=r".. method:: I2C.writeto(addr, buf, stop=True, /)",
        new="def writeto(self, addr: int, buf: AnyReadableBuf, stop: bool = True, /) -> int",
        extra_docs=standard_docs,
    )
    shed.def_(
        old=r".. method:: I2C.writevto(addr, vector, stop=True, /)",
        new="""
def writevto(
   self, 
   addr: int, 
   vector: Sequence[AnyReadableBuf], 
   stop: bool = True, 
   /
) -> int
""",
        extra_docs=standard_docs,
        end="Memory operations",
    )
    memory_docs = shed.extra_docs()
    shed.def_(
        old=r".. method:: I2C.readfrom_mem(addr, memaddr, nbytes, *, addrsize=8)",
        new="def readfrom_mem(self, addr: int, memaddr: int, nbytes: int, /, *, addrsize: int = 8) -> bytes",
        extra_docs=memory_docs,
    )
    shed.def_(
        old=r".. method:: I2C.readfrom_mem_into(addr, memaddr, buf, *, addrsize=8)",
        new="""
def readfrom_mem_into(
   self, 
   addr: int, 
   memaddr: int, 
   buf: AnyWritableBuf, 
   /, 
   *, 
   addrsize: int = 8
) -> None
""",
        extra_docs=memory_docs,
    )
    i2s = "machine.I2S.rst"
    shed.def_(
        old=r".. method:: I2C.writeto_mem(addr, memaddr, buf, *, addrsize=8",
        new="def writeto_mem(self, addr: int, memaddr: int, buf: AnyReadableBuf, /, *, addrsize: int = 8) -> None",
        extra_docs=memory_docs,
        end=i2s,
    )
    return i2s


def _spi(this: str, shed: RST2PyI) -> str:
    shed.class_from_file(old=this)
    shed.def_(
        old=".. class:: SPI(id, ...)",
        new=[
            """
def __init__(self, id: int, /)
""",
            """
def __init__(
   self, 
   id: int, 
   /, 
   baudrate: int = 1_000_000, 
   *,
   polarity: int = 0, 
   phase: int = 0, 
   bits: int = 8, 
   firstbit: int = MSB, 
   sck: Pin | None = None, 
   mosi: Pin | None = None, 
   miso: Pin | None = None, 
)
""",
            """
def __init__(
   self, 
   id: int, 
   /, 
   baudrate: int = 1_000_000, 
   *,
   polarity: int = 0, 
   phase: int = 0, 
   bits: int = 8, 
   firstbit: int = MSB, 
   pins: tuple[Pin, Pin, Pin] | None = None, 
)
""",
        ],
    )
    shed.def_(
        old=(
            r".. method:: SPI.init(baudrate=1000000, *, polarity=0, phase=0, bits=8, "
            r"firstbit=SPI.MSB, sck=None, mosi=None, miso=None, pins=(SCK, MOSI, MISO))"
        ),
        new=[
            """
def init(
   self, 
   baudrate: int = 1_000_000, 
   *,
   polarity: int = 0, 
   phase: int = 0, 
   bits: int = 8, 
   firstbit: int = MSB, 
   sck: Pin | None = None, 
   mosi: Pin | None = None, 
   miso: Pin | None = None, 
) -> None
""",
            """
def init(
   self, 
   baudrate: int = 1_000_000, 
   *,
   polarity: int = 0, 
   phase: int = 0, 
   bits: int = 8, 
   firstbit: int = MSB, 
   pins: tuple[Pin, Pin, Pin] | None = None, 
) -> None
""",
        ],
    )
    shed.def_(
        old=r".. method:: SPI.deinit()", new="def deinit(self) -> None",
    )
    shed.def_(
        old=r".. method:: SPI.read(nbytes, write=0x00)",
        new="def read(self, nbytes: int, write: int = 0x00, /) -> bytes",
    )
    shed.def_(
        old=r".. method:: SPI.readinto(buf, write=0x00)",
        new="def readinto(self, buf: AnyWritableBuf, write: int = 0x00, /) -> int | None",
    )
    shed.def_(
        old=r".. method:: SPI.write(buf)",
        new="def write(self, buf: AnyReadableBuf, /) -> int | None",
    )
    shed.def_(
        old=r".. method:: SPI.write_readinto(write_buf, read_buf)",
        new="def write_readinto(self, write_buf: AnyReadableBuf, read_buf: AnyWritableBuf, /) -> int | None",
    )
    shed.vars(old=".. data:: SPI.CONTROLLER")
    shed.vars(old=".. data:: SPI.MSB")
    nxt = "machine.I2C.rst"
    shed.vars(old=".. data:: SPI.LSB", end=nxt)
    return nxt


def _uart(this: str, shed: RST2PyI) -> str:
    shed.class_from_file(old=this, end="Constructors")
    shed.def_(
        old=".. class:: UART(id, ...)",
        new=[
            """
def __init__(
   self,
   id: int | str,
   baudrate: int = 9600, 
   bits: int = 8, 
   parity: int | None = None, 
   stop: int = 1, 
   /, 
   *, 
   tx: Pin | None = None,
   rx: Pin | None = None,
   txbuf: int | None = None,
   rxbuf: int | None = None,
   timeout: int | None = None,
   timeout_char: int | None = None,
   invert: int | None = None,
)
""",
            """
def __init__(
   self,
   id: int | str,
   baudrate: int = 9600, 
   bits: int = 8, 
   parity: int | None = None, 
   stop: int = 1, 
   /, 
   *, 
   pins: tuple[Pin, Pin] | None = None,
)
""",
            """
def __init__(
   self,
   id: int | str,
   baudrate: int = 9600, 
   bits: int = 8, 
   parity: int | None = None, 
   stop: int = 1, 
   /, 
   *, 
   pins: tuple[Pin, Pin, Pin, Pin] | None = None,
)
""",
        ],
        end="Methods",
    )
    shed.def_(
        old=".. method:: UART.init(baudrate=9600, bits=8, parity=None, stop=1, *, ...)",
        new=[
            """
def init(
   self,
   baudrate: int = 9600, 
   bits: int = 8, 
   parity: int | None = None, 
   stop: int = 1, 
   /, 
   *, 
   tx: Pin | None = None,
   rx: Pin | None = None,
   txbuf: int | None = None,
   rxbuf: int | None = None,
   timeout: int | None = None,
   timeout_char: int | None = None,
   invert: int | None = None,
) -> None
""",
            """
def init(
   self,
   baudrate: int = 9600, 
   bits: int = 8, 
   parity: int | None = None, 
   stop: int = 1, 
   /, 
   *, 
   pins: tuple[Pin, Pin] | None = None,
) -> None
""",
            """
def init(
   self,
   baudrate: int = 9600, 
   bits: int = 8, 
   parity: int | None = None, 
   stop: int = 1, 
   /, 
   *, 
   pins: tuple[Pin, Pin, Pin, Pin] | None = None,
) -> None
""",
        ],
    )
    shed.def_(
        old=".. method:: UART.deinit()", new="def deinit(self) -> None",
    )
    shed.def_(
        old=".. method:: UART.any()", new="def any(self) -> int",
    )
    shed.def_(
        old=".. method:: UART.read([nbytes])",
        new=[
            "def read(self) -> bytes | None",
            "def read(self, nbytes: int, /) -> bytes | None",
        ],
    )
    shed.def_(
        old=".. method:: UART.readinto(buf[, nbytes])",
        new=[
            "def readinto(self, buf: AnyWritableBuf, /) -> int | None",
            "def readinto(self, buf: AnyWritableBuf, nbytes: int, /) -> int | None",
        ],
    )
    shed.def_(
        old=".. method:: UART.readline()", new="def readline(self) -> bytes | None",
    )
    shed.def_(
        old=".. method:: UART.write(buf)",
        new="def write(self, buf: AnyReadableBuf, /) -> int | None",
    )
    shed.def_(
        old=".. method:: UART.sendbreak()", new="def sendbreak(self) -> None",
    )
    shed.def_(
        old=".. method:: UART.irq(trigger, priority=1, handler=None, wake=machine.IDLE)",
        new="""
def irq(
   self, 
   trigger: int, 
   priority: int = 1, 
   handler: Callable[[UART], None] | None = None, 
   wake: int = IDLE, 
   /
) -> Any
""",
        end="Constants",
    )
    nxt = "machine.SPI.rst"
    shed.vars(
        old=".. data:: UART.RX_ANY", end=nxt,
    )
    return nxt


def _adc(this: str, shed: RST2PyI) -> str:
    shed.class_from_file(old=this)
    shed.def_(
        old=".. class:: ADC(id)",
        new="def __init__(self, pin: int | Pin, /)",
        extra_docs=[
            ".. note::",
            "",
            "WiPy has a custom implementation of ADC, see ADCWiPy for details.",
        ],
    )
    nxt = "machine.PWM.rst"
    shed.def_(
        old=".. method:: ADC.read_u16()", new="def read_u16(self) -> int", end=nxt
    )
    return nxt


def _signal(this: str, shed: RST2PyI) -> str:
    shed.class_from_file(old=this)
    shed.defs_with_common_description(
        cmd=".. class:: ",
        old2new={
            r"Signal(pin_obj, invert=False)": """
@overload
def __init__(self, pin_obj: Pin, invert: bool = False, /)
""",
            r"Signal(pin_arguments..., *, invert=False)": """
@overload
def __init__(
   self, 
   id: Pin | str, 
   /, 
   mode: int = -1, 
   pull: int = -1, 
   *, 
   value: Any = None,
   drive: int | None = None,
   alt: int | None = None,
   invert: bool = False,
)
""",
        },
        end="Methods",
    )
    shed.def_(
        old=r".. method:: Signal.value([x])",
        new=["def value(self) -> int", "def value(self, x: Any, /) -> None"],
    )
    shed.def_(
        old=r".. method:: Signal.on()", new="def on(self) -> None",
    )
    nxt = "machine.ADC.rst"
    shed.def_(old=r".. method:: Signal.off()", new="def off(self) -> None", end=nxt)
    return nxt


def _pin(shed: RST2PyI) -> str:
    pin: Final = r"machine.Pin.rst"
    shed.consume_up_to_but_excl_end_line(end=pin)
    shed.class_from_file(
        old=pin, end="Constructors",
    )
    shed.def_(
        old=".. class:: Pin(id, mode=-1, pull=-1, *, value, drive, alt)",
        new="""
def __init__(
   self, 
   id: Any, 
   /,
   mode: int = -1, 
   pull: int = -1, 
   *,
   value: Any = None,
   drive: int | None = None,
   alt: int | None = None
)
""",
        end="Methods",
    )
    shed.def_(
        old=".. method:: Pin.init(mode=-1, pull=-1, *, value, drive, alt)",
        new="""
def init(
   self, 
   mode: int = -1, 
   pull: int = -1, 
   *,
   value: Any = None,
   drive: int | None = None,
   alt: int | None = None
) -> None
""",
    )
    shed.def_(
        old=".. method:: Pin.value([x])",
        new=["def value(self) -> int", "def value(self, x: Any, /) -> None"],
    )
    shed.def_(
        old=".. method:: Pin.__call__([x])",
        new=["def __call__(self) -> int", "def __call__(self, x: Any, /) -> None"],
    )
    shed.def_(old=".. method:: Pin.on()", new="def on(self) -> None")
    shed.def_(old=".. method:: Pin.off()", new="def off(self) -> None")
    shed.def_(
        old=(
            ".. method:: Pin.irq(handler=None, trigger=(Pin.IRQ_FALLING | Pin.IRQ_RISING), *, "
            "priority=1, wake=None, hard=False)"
        ),
        new="""
def irq(
   self,
   /,
   handler: Callable[[Pin], None] | None = None, 
   trigger: int = (IRQ_FALLING | IRQ_RISING), 
   *, 
   priority: int = 1, 
   wake: int | None = None, 
   hard: bool = False,
) -> Callable[[Pin], None] | None
""",
        end="The following methods are not part of the core Pin API and only implemented on certain ports.",
    )
    low = ".. method:: Pin.low()"
    shed.consume_up_to_but_excl_end_line(end=low)
    shed.def_(old=low, new="def low(self) -> None")
    shed.def_(old=".. method:: Pin.high()", new="def high(self) -> None")
    shed.def_(
        old=".. method:: Pin.mode([mode])",
        new=["def mode(self) -> int", "def mode(self, mode: int, /) -> None"],
    )
    shed.def_(
        old=".. method:: Pin.pull([pull])",
        new=["def pull(self) -> int", "def pull(self, pull: int, /) -> None"],
    )
    shed.def_(
        old=".. method:: Pin.drive([drive])",
        new=["def dive(self) -> int", "def drive(self, drive: int, /) -> None"],
    )
    shed.vars(
        old=[
            ".. data:: Pin.IN",
            "Pin.OUT",
            "Pin.OPEN_DRAIN",
            "Pin.ALT",
            "Pin.ALT_OPEN_DRAIN",
            "Pin.ANALOG",
        ],
    )
    shed.vars(old=[".. data:: Pin.PULL_UP", "Pin.PULL_DOWN", "Pin.PULL_HOLD"],)
    shed.vars(old=[".. data:: Pin.LOW_POWER", "Pin.MED_POWER", "Pin.HIGH_POWER"],)
    nxt = "machine.Signal.rst"
    shed.vars(
        old=[
            ".. data:: Pin.IRQ_FALLING",
            "Pin.IRQ_RISING",
            "Pin.IRQ_LOW_LEVEL",
            "Pin.IRQ_HIGH_LEVEL",
        ],
        end=nxt,
    )
    return nxt


def _machine(shed: RST2PyI) -> None:
    module_post_doc = f"""
from typing import overload, NoReturn, Callable
from typing import Sequence, ClassVar, Any, Final

from uos import AbstractBlockDev
from uio import AnyReadableBuf, AnyWritableBuf
"""
    shed.module(
        name="machine",
        old="functions related to the hardware",
        post_doc=module_post_doc,
        end="The ``machine`` module contains specific functions related to the hardware",
    )
    shed.pyi.doc.extend(shed.extra_notes(end="Reset related functions"))
    shed.def_(old=".. function:: reset()", new="def reset() -> NoReturn", indent=0)
    shed.def_(
        old=".. function:: soft_reset()", new="def soft_reset() -> NoReturn", indent=0
    )
    shed.def_(
        old=".. function:: reset_cause()", new="def reset_cause() -> int", indent=0
    )
    shed.def_(
        old=".. function:: disable_irq()", new="def disable_irq() -> bool", indent=0
    )
    shed.def_(
        old=".. function:: enable_irq(state)",
        new="def enable_irq(state: bool = True, /) -> None",
        indent=0,
    )
    shed.def_(
        old=".. function:: freq([hz])",
        new=["def freq() -> int", "def freq(hz: int, /) -> None"],
        indent=0,
    )
    shed.def_(old=".. function:: idle()", new="def idle() -> None", indent=0)
    shed.def_(old=".. function:: sleep()", new="def sleep() -> None", indent=0)
    wake_reason = ".. function:: wake_reason()"
    shed.defs_with_common_description(
        cmd=".. function:: ",
        old2new={
            "lightsleep([time_ms])": [
                "def lightsleep() -> None",
                "def lightsleep(time_ms: int, /) -> None",
            ],
            "deepsleep([time_ms])": [
                "def deepsleep() -> NoReturn",
                "def deepsleep(time_ms: int, /) -> NoReturn",
            ],
        },
        end=wake_reason,
        indent=0,
    )
    shed.def_(old=wake_reason, new="def wake_reason() -> int", indent=0)
    shed.def_(old=".. function:: unique_id()", new="def unique_id() -> bytes", indent=0)
    shed.def_(
        old=".. function:: time_pulse_us(pin, pulse_level, timeout_us=1000000, /)",
        new="def time_pulse_us(pin: Pin, pulse_level: int, timeout_us: int = 1_000_000, /) -> int",
        indent=0,
    )
    shed.def_(old=".. function:: rng()", new="def rng() -> int", indent=0)
    idle = ".. data:: machine.IDLE"
    shed.consume_up_to_but_excl_end_line(end=idle)
    shed.vars(
        old=[".. data:: machine.IDLE", "machine.SLEEP", "machine.DEEPSLEEP"],
        class_var=None,
    )
    shed.vars(
        old=[
            ".. data:: machine.PWRON_RESET",
            "machine.HARD_RESET",
            "machine.WDT_RESET",
            "machine.DEEPSLEEP_RESET",
            "machine.SOFT_RESET",
        ],
        class_var=None,
    )
    shed.vars(
        old=[".. data:: machine.WLAN_WAKE", "machine.PIN_WAKE", "machine.RTC_WAKE"],
        class_var=None,
        end="Classes",
    )
