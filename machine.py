"""
Generate `pyi` from corresponding `rst` docs.
"""

import repdefs
import rst
from rst2pyi import RST2PyI

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = "3.6.0"  # Version set by https://github.com/hlovatt/tag2ver


def machine(shed: RST2PyI) -> None:
    _machine(shed)
    nxt = _pin(shed)
    nxt = _signal(nxt, shed)
    nxt = _adc(nxt, shed)
    nxt = _uart(nxt, shed)
    nxt = _spi(nxt, shed)
    nxt = _i2c(nxt, shed)
    nxt = _rtc(nxt, shed)
    nxt = _timer(nxt, shed)
    nxt = _wdt(nxt, shed)
    nxt = _sd(nxt, shed)
    _sd_card(nxt, shed)

    shed.write()


def _sd_card(this: str, shed: RST2PyI) -> None:
    con = '.. class:: SDCard(slot=1, width=1, cd=None, wp=None, sck=None, miso=None, mosi=None, cs=None, freq=20000000)'
    shed.class_from_file(old=this, super_class='_AbstractBlockDev', end=con)
    shed.def_(
        old=con,
        new='''
def __init__(
   self, 
   slot: int = 1, 
   width: int = 1, 
   cd: Optional[Union[int, str, Pin]] = None, 
   wp: Optional[Union[int, str, Pin]] = None, 
   sck: Optional[Union[int, str, Pin]] = None, 
   miso: Optional[Union[int, str, Pin]] = None, 
   mosi: Optional[Union[int, str, Pin]] = None, 
   cs: Optional[Union[int, str, Pin]] = None, 
   freq: int = 20000000
)
''',
        end='Implementation-specific details',
    )
    shed.pyi.classes[-1].defs.append('''
   def readblocks(self, blocknum: int, buf: bytes, offset: int = 0, /) -> None: ... 
   
   def writeblocks(self, blocknum: int, buf: bytes, offset: int = 0, /) -> None: ...
   
   def ioctl(self, op: int, arg: int) -> Optional[int]: ...
''')
    shed.pyi.classes[-1].doc += shed.extra_docs()


def _sd(this: str, shed: RST2PyI) -> str:
    shed.class_from_file(old=this,)
    shed.def_(
        old=r'.. class:: SD(id,... )',
        new='''
def __init__(
   self, 
   id: int = 0, 
   pins: Union[Tuple[str, str, str], Tuple[Pin, Pin, Pin]] = ("GP10", "GP11", "GP15")
)
''')
    shed.def_(
        old=r".. method:: SD.init(id=0, pins=('GP10', 'GP11', 'GP15'))",
        new='''
def init(
   self, 
   id: int = 0, 
   pins: Union[Tuple[str, str, str], Tuple[Pin, Pin, Pin]] = ("GP10", "GP11", "GP15")
) -> None
''',
    )
    nxt = 'machine.SDCard.rst'
    shed.def_(
        old=r'.. method:: SD.deinit()',
        new='def deinit(self) -> None',
        end=nxt,
    )
    return nxt


def _wdt(this: str, shed: RST2PyI) -> str:
    shed.class_from_file(old=this,)
    shed.def_(
        old='.. class:: WDT(id=0, timeout=5000)',
        new='def __init__(self, *, id: int = 0, timeout: int = 5000)',
    )
    nxt = 'machine.SD.rst'
    shed.def_(
        old='.. method:: wdt.feed()',
        new='def feed(self) -> None',
        end=nxt,
    )
    return nxt


def _timer(this: str, shed: RST2PyI) -> str:
    shed.class_from_file(old=this,)
    shed.def_(
        old=r'.. class:: Timer(id, ...)',
        new=['''
def __init__(
   self, 
   id: int, 
   /
)
''', '''
def __init__(
   self, 
   id: int, 
   /, 
   *, 
   mode: int = PERIODIC, 
   period: int = -1, 
   callback: Optional[Callable[["Timer"], None]] = None, 
)
'''],
    )
    shed.def_(
        old=r'.. method:: Timer.init(*, mode=Timer.PERIODIC, period=-1, callback=None)',
        new='''
def init(
   self, 
   *, 
   mode: int = PERIODIC, 
   period: int = -1, 
   callback: Optional[Callable[["Timer"], None]] = None, 
) -> None
''',
    )
    shed.def_(
        old=r'.. method:: Timer.deinit()',
        new='def deinit(self) -> None',
    )
    nxt = 'machine.WDT.rst'
    shed.vars(class_var=True, end=nxt)
    return nxt


def _rtc(_: str, shed: RST2PyI) -> str:
    shed.pyi.imports_vars_defs.append('RTC: Type[pyb.RTC] = pyb.RTC\n')
    nxt = 'machine.Timer.rst'
    shed.consume(end=nxt)
    return nxt


def _i2c(this: str, shed: RST2PyI) -> str:
    shed.class_from_file(old=this, )
    shed.def_(
        old=r'.. class:: I2C(id, *, scl, sda, freq=400000)',
        new=[
            'def __init__(self, id: int, /, *, freq: int = 400_000)',
            'def __init__(self, id: int, /, *, scl: Pin, sda: Pin, freq: int = 400_000)',
        ],
    )
    shed.def_(
        old=r'.. method:: I2C.init(scl, sda, *, freq=400000)',
        new=[
            'def init(self, *, freq: int = 400_000) -> None',
            'def init(self, *, scl: Pin, sda: Pin, freq: int = 400_000) -> None',
        ],
    )
    shed.def_(
        old=r'.. method:: I2C.deinit()',
        new='def deinit(self) -> None',
    )
    primitive_docs_start = 'Primitive I2C operations'
    shed.def_(
        old=r'.. method:: I2C.scan()',
        new='def scan(self) -> List[int]',
        end=primitive_docs_start
    )
    primitive_docs = shed.extra_docs()
    shed.def_(
        old=r'.. method:: I2C.start()',
        new='def start(self) -> None',
        extra_docs=primitive_docs
    )
    shed.def_(
        old=r'.. method:: I2C.stop()',
        new='def stop(self) -> None',
        extra_docs=primitive_docs
    )
    shed.def_(
        old=r'.. method:: I2C.readinto(buf, nack=True, /)',
        new='def readinto(self, buf: _AnyWritableBuf, nack: bool = True, /) -> None',
        extra_docs=primitive_docs
    )
    shed.def_(
        old=r'.. method:: I2C.write(buf)',
        new='def write(self, buf: _AnyReadableBuf, /) -> int',
        extra_docs=primitive_docs,
        end='Standard bus operations',
    )
    standard_docs = shed.extra_docs()
    shed.def_(
        old=r'.. method:: I2C.readfrom(addr, nbytes, stop=True, /)',
        new='def readfrom(self, addr: int, nbytes: int, stop: bool = True, /) -> bytes',
        extra_docs=standard_docs
    )
    shed.def_(
        old=r'.. method:: I2C.readfrom_into(addr, buf, stop=True, /)',
        new='def readfrom_into(self, addr: int, buf: _AnyWritableBuf, stop: bool = True, /) -> None',
        extra_docs=standard_docs
    )
    shed.def_(
        old=r'.. method:: I2C.writeto(addr, buf, stop=True, /)',
        new='def writeto(self, addr: int, buf: _AnyWritableBuf, stop: bool = True, /) -> int',
        extra_docs=standard_docs
    )
    shed.def_(
        old=r'.. method:: I2C.writevto(addr, vector, stop=True, /)',
        new='''
def writevto(
   self, 
   addr: int, 
   vector: Sequence[_AnyReadableBuf], 
   stop: bool = True, 
   /
) -> int
''',
        extra_docs=standard_docs,
        end='Memory operations',
    )
    memory_docs = shed.extra_docs()
    shed.def_(
        old=r'.. method:: I2C.readfrom_mem(addr, memaddr, nbytes, *, addrsize=8)',
        new='def readfrom_mem(self, addr: int, memaddr: int, nbytes: int, /, *, addrsize: int = 8) -> bytes',
        extra_docs=memory_docs
    )
    shed.def_(
        old=r'.. method:: I2C.readfrom_mem_into(addr, memaddr, buf, *, addrsize=8)',
        new='''
def readfrom_mem_into(
   self, 
   addr: int, 
   memaddr: int, 
   buf: _AnyWritableBuf, 
   /, 
   *, 
   addrsize: int = 8
) -> None
''',
        extra_docs=memory_docs
    )
    rtc = 'machine.RTC.rst'
    shed.def_(
        old=r'.. method:: I2C.writeto_mem(addr, memaddr, buf, *, addrsize=8',
        new='def writeto_mem(self, addr: int, memaddr: int, buf: _AnyReadableBuf, /, *, addrsize: int = 8) -> None',
        extra_docs=memory_docs,
        end=rtc
    )
    return rtc


def _spi(this: str, shed: RST2PyI) -> str:
    shed.class_from_file(old=this)
    shed.def_(
        old='.. class:: SPI(id, ...)',
        new=['''
def __init__(self, id: int, /)
''', '''
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
   sck: Optional[Pin] = None, 
   mosi: Optional[Pin] = None, 
   miso: Optional[Pin] = None, 
)
''', '''
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
   pins: Optional[Tuple[Pin, Pin, Pin]] = None, 
)
'''],
    )
    shed.def_(
        old=(
            r'.. method:: SPI.init(baudrate=1000000, *, polarity=0, phase=0, bits=8, '
            r'firstbit=SPI.MSB, sck=None, mosi=None, miso=None, pins=(SCK, MOSI, MISO))'
        ),
        new=['''
def init(
   self, 
   baudrate: int = 1_000_000, 
   *,
   polarity: int = 0, 
   phase: int = 0, 
   bits: int = 8, 
   firstbit: int = MSB, 
   sck: Optional[Pin] = None, 
   mosi: Optional[Pin] = None, 
   miso: Optional[Pin] = None, 
) -> None
''', '''
def init(
   self, 
   baudrate: int = 1_000_000, 
   *,
   polarity: int = 0, 
   phase: int = 0, 
   bits: int = 8, 
   firstbit: int = MSB, 
   pins: Optional[Tuple[Pin, Pin, Pin]] = None, 
) -> None
'''],
    )
    shed.def_(
        old=r'.. method:: SPI.deinit()',
        new='def deinit(self) -> None',
    )
    shed.def_(
        old=r'.. method:: SPI.read(nbytes, write=0x00)',
        new='def read(self, nbytes: int, write: int = 0x00, /) -> bytes',
    )
    shed.def_(
        old=r'.. method:: SPI.readinto(buf, write=0x00)',
        new='def readinto(self, buf: _AnyWritableBuf, write: int = 0x00, /) -> Optional[int]',
    )
    shed.def_(
        old=r'.. method:: SPI.write(buf)',
        new='def write(self, buf: _AnyReadableBuf, /) -> Optional[int]',
    )
    shed.def_(
        old=r'.. method:: SPI.write_readinto(write_buf, read_buf)',
        new='def write_readinto(self, write_buf: _AnyReadableBuf, read_buf: _AnyWritableBuf, /) -> Optional[int]',
    )
    nxt = 'machine.I2C.rst'
    shed.vars(end=nxt)
    return nxt


def _uart(_: str, shed: RST2PyI) -> str:
    shed.pyi.imports_vars_defs.append('UART: Type[pyb.UART] = pyb.UART\n')
    nxt = 'machine.SPI.rst'
    shed.consume(end=nxt)
    return nxt


def _adc(this: str, shed: RST2PyI) -> str:
    shed.class_from_file(old=this)
    shed.def_(
        old='.. class:: ADC(id)',
        new='def __init__(self, pin: Union[int, Pin], /)',
    )
    nxt = 'machine.UART.rst'
    shed.def_(
        old='.. method:: ADC.read_u16()',
        new='def read_u16(self) -> int',
        end=nxt
    )
    return nxt


def _signal(this: str, shed: RST2PyI) -> str:
    shed.class_from_file(old=this)
    shed.defs_with_common_description(
        cmd='.. class:: ',
        old2new={
            r'Signal(pin_obj, invert=False)':
                '''
@overload
def __init__(self, pin_obj: Pin, invert: bool = False, /)
''',
            r'Signal(pin_arguments..., *, invert=False)':
                '''
@overload
def __init__(
   self, 
   id: Union[Pin, str], 
   /, 
   mode: int = Pin.IN, 
   pull: int = Pin.PULL_NONE, 
   af: Union[str, int] = -1, 
   *, 
   invert: bool = False
)
''',
        },
        end='Methods',
    )
    shed.def_(
        old=r'.. method:: Signal.value([x])',
        new=[
            'def value(self) -> int',
            'def value(self, x: int) -> None'
        ],
    )
    shed.def_(
        old=r'.. method:: Signal.on()',
        new='def on(self) -> None',
    )
    nxt = 'machine.ADC.rst'
    shed.def_(
        old=r'.. method:: Signal.off()',
        new='def off(self) -> None',
        end=nxt
    )
    return nxt


def _pin(shed: RST2PyI) -> str:
    shed.pyi.imports_vars_defs.append('Pin: Type[pyb.Pin] = pyb.Pin\n')
    nxt = 'machine.Signal.rst'
    shed.consume(end=nxt)
    return nxt


def _machine(shed: RST2PyI) -> None:
    module_post_doc = f'''
from abc import abstractmethod
from typing import overload, Union, Tuple, TypeVar, Optional, NoReturn, List, Callable
from typing import Type, Sequence, runtime_checkable, Protocol, ClassVar

import pyb
from uarray import array


{repdefs.AbstractBlockDev}


{repdefs.AnyWritableBuf}


{repdefs.AnyReadableBuf}
'''
    shed.module(
        name='machine',
        old='functions related to the hardware',
        post_doc=module_post_doc,
        end='The ``machine`` module contains specific functions related to the hardware'
    )
    shed.pyi.doc += shed.extra_notes(end='Reset related functions')
    shed.def_(
        old='.. function:: reset()',
        new='def reset() -> NoReturn',
        indent=0
    )
    shed.def_(
        old='.. function:: soft_reset()',
        new='def soft_reset() -> NoReturn',
        indent=0
    )
    shed.def_(
        old='.. function:: reset_cause()',
        new='def reset_cause() -> int',
        indent=0
    )
    shed.def_(
        old='.. function:: disable_irq()',
        new='def disable_irq() -> bool',
        indent=0
    )
    shed.def_(
        old='.. function:: enable_irq(state)',
        new='def enable_irq(state: bool = True, /) -> None',
        indent=0
    )
    shed.def_(
        old='.. function:: freq()',
        new='def freq() -> int',
        indent=0
    )
    shed.def_(
        old='.. function:: idle()',
        new='def idle() -> None',
        indent=0
    )
    shed.def_(
        old='.. function:: sleep()',
        new='def sleep() -> None',
        indent=0
    )
    wake_reason = '.. function:: wake_reason()'
    shed.defs_with_common_description(
        cmd='.. function:: ',
        old2new={
            'lightsleep([time_ms])': [
                'def lightsleep() -> None',
                'def lightsleep(time_ms: int, /) -> None',
            ],
            'deepsleep([time_ms])': [
                'def deepsleep() -> NoReturn',
                'def deepsleep(time_ms: int, /) -> NoReturn',
            ],
        },
        end=wake_reason,
        indent=0
    )
    shed.def_(
        old=wake_reason,
        new='def wake_reason() -> int',
        indent=0
    )
    shed.def_(
        old='.. function:: unique_id()',
        new='def unique_id() -> bytes',
        indent=0
    )
    shed.def_(
        old='.. function:: time_pulse_us(pin, pulse_level, timeout_us=1000000, /)',
        new='def time_pulse_us(pin: Pin, pulse_level: int, timeout_us: int = 1_000_000, /) -> int',
        indent=0
    )
    shed.def_(
        old='.. function:: rng()',
        new='def rng() -> int',
        indent=0
    )
    shed.consume(end='.. data:: machine.IDLE')
    shed.vars(class_var=None, end='Classes')
