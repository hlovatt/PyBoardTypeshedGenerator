"""
Generate `pyi` from corresponding `rst` docs.
"""

import repdefs
import rst
from class_ import Class
from rst2pyi import RST2PyI

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = "3.7.2"  # Version set by https://github.com/hlovatt/tag2ver


def pyb(shed: RST2PyI) -> None:
    _pyb(shed)
    nxt = _accel(shed)
    nxt = _adc(nxt, shed)
    nxt = _can(nxt, shed)
    nxt = _dac(nxt, shed)
    nxt = _ext_int(nxt, shed)
    nxt = _flash(nxt, shed)
    nxt = _i2c(nxt, shed)
    nxt = _lcd(nxt, shed)
    nxt = _led(nxt, shed)
    nxt = _pin(nxt, shed)
    nxt = _rtc(nxt, shed)
    nxt = _servo(nxt, shed)
    nxt = _spi(nxt, shed)
    nxt = _switch(nxt, shed)
    nxt = _timer(nxt, shed)
    nxt = _uart(nxt, shed)
    nxt = _usb_hid(nxt, shed)
    _usb_vcp(nxt, shed)

    shed.write()


def _usb_vcp(this: str, shed: RST2PyI) -> None:
    shed.class_from_file(old=this)
    shed.def_(
        old=r'.. class:: pyb.USB_VCP(id=0)',
        new='def __init__(self, id: int = 0, /)',
    )
    shed.def_(
        old=r'.. method:: USB_VCP.init(*, flow=-1)',
        new='def init(self, *, flow: int = - 1) -> int',
    )
    shed.def_(
        old=r'.. method:: USB_VCP.setinterrupt(chr)',
        new='def setinterrupt(self, chr: int, /) -> None',
    )
    shed.def_(
        old=r'.. method:: USB_VCP.isconnected()',
        new='def isconnected(self) -> bool',
    )
    shed.def_(
        old=r'.. method:: USB_VCP.any()',
        new='def any(self) -> bool',
    )
    shed.def_(
        old=r'.. method:: USB_VCP.close()',
        new='def close(self) -> None',
    )
    shed.def_(
        old=r'.. method:: USB_VCP.read([nbytes])',
        new=[
            'def read(self) -> Optional[bytes]',
            'def read(self, nbytes, /) -> Optional[bytes]'
        ],
    )
    shed.def_(
        old=r'.. method:: USB_VCP.readinto(buf, [maxlen])',
        new=[
            'def readinto(self, buf: _AnyWritableBuf, /) -> Optional[int]',
            'def readinto(self, buf: _AnyWritableBuf, maxlen: int, /) -> Optional[int]'
        ],
    )
    shed.def_(
        old=r'.. method:: USB_VCP.readline()',
        new='def readline(self) -> Optional[bytes]',
    )
    shed.def_(
        old=r'.. method:: USB_VCP.readlines()',
        new='def readlines(self) -> Optional[List[bytes]]',
    )
    shed.def_(
        old=r'.. method:: USB_VCP.write(buf)',
        new='def write(self, buf: _AnyReadableBuf, /) -> int',
    )
    shed.def_(
        old=r'.. method:: USB_VCP.recv(data, *, timeout=5000)',
        new=[
            'def recv(self, data: int, /, *, timeout: int = 5000) -> Optional[bytes]',
            'def recv(self, data: _AnyWritableBuf, /, *, timeout: int = 5000) -> Optional[int]'
        ],
    )
    shed.def_(
        old=r'.. method:: USB_VCP.send(data, *, timeout=5000)',
        new='def send(self, buf: Union[_AnyWritableBuf, bytes, int], /, *, timeout: int = 5000) -> int',
    )
    shed.vars(end=None)


def _usb_hid(this: str, shed: RST2PyI) -> str:
    shed.class_from_file(old=this)
    shed.def_(
        old=r'.. class:: pyb.USB_HID()',
        new='def __init__(self)',
    )
    shed.def_(
        old=r'.. method:: USB_HID.recv(data, *, timeout=5000)',
        new=[
            'def recv(self, data: int, /, *, timeout: int = 5000) -> bytes',
            'def recv(self, data: _AnyWritableBuf, /, *, timeout: int = 5000) -> int'
        ],
    )
    nxt = 'pyb.USB_VCP.rst'
    shed.def_(
        old=r'.. method:: USB_HID.send(data)',
        new='def send(self, data: Sequence[int]) -> None',
        end=nxt
    )
    return nxt


def _uart(this: str, shed: RST2PyI) -> str:
    shed.class_from_file(
        pre_str='# noinspection PyShadowingNames',
        old=this,
    )
    shed.def_(
        old=r'.. class:: pyb.UART(bus, ...)',
        new=['''
def __init__(
   self, 
   bus: Union[int, str],
   /
)''', '''
def __init__(
   self, 
   bus: Union[int, str],
   baudrate: int,
   /,
   bits: int = 8,
   parity: Optional[int] = None, 
   stop: int = 1, 
   *, 
   timeout: int = 0, 
   flow: int = 0, 
   timeout_char: int = 0, 
   read_buf_len: int = 64
)
'''],
    )
    shed.def_(
        old=(
            r'.. method:: UART.init(baudrate, bits=8, parity=None, stop=1, *, '
            r'timeout=0, flow=0, timeout_char=0, read_buf_len=64)'
        ),
        new='''
def init(
   self, 
   baudrate: int,
   /,
   bits: int = 8,
   parity: Optional[int] = None, 
   stop: int = 1, 
   *, 
   timeout: int = 0, 
   flow: int = 0, 
   timeout_char: int = 0, 
   read_buf_len: int = 64
)
''',
    )
    shed.def_(
        old=r'.. method:: UART.deinit()',
        new='def deinit(self) -> None',
    )
    shed.def_(
        old=r'.. method:: UART.any()',
        new='def any(self) -> int',
    )
    shed.def_(
        old=r'.. method:: UART.read([nbytes])',
        new=[
            'def read(self) -> Optional[bytes]',
            'def read(self, nbytes: int, /) -> Optional[bytes]'
        ],
    )
    shed.def_(
        old=r'.. method:: UART.readchar()',
        new='def readchar(self) -> int',
    )
    shed.def_(
        old=r'.. method:: UART.readinto(buf[, nbytes])',
        new=[
            'def readinto(self, buf: _AnyWritableBuf, /) -> Optional[int]',
            'def readinto(self, buf: _AnyWritableBuf, nbytes: int, /) -> Optional[int]'
        ],
    )
    shed.def_(
        old=r'.. method:: UART.readline()',
        new='def readline(self) -> Optional[str]',
    )
    shed.def_(
        old=r'.. method:: UART.write(buf)',
        new='def write(self, buf: _AnyWritableBuf, /) -> Optional[int]',
    )
    shed.def_(
        old=r'.. method:: UART.writechar(char)',
        new='def writechar(self, char: int, /) -> None',
    )
    shed.def_(
        old=r'.. method:: UART.sendbreak()',
        new='def sendbreak(self) -> None',
    )
    shed.vars(end='Flow Control')
    nxt = 'pyb.USB_HID.rst'
    shed.pyi.doc += shed.extra_notes(end=nxt)
    return nxt


def _timer_channel(*, old: str, end: str, shed: RST2PyI) -> None:
    shed.consume_name_line(old)
    shed.consume_title_line()
    shed.consume_blank_line()
    methods = 'Methods'
    doc = []
    for doc_line in shed.rst:
        if doc_line.startswith(methods):
            shed.consume_header_line()
            shed.consume_blank_line()
            break
        doc.append(f'   {doc_line}\n')
    else:
        assert False, f'Did not find: `{methods}`'
    new_class = Class()
    new_class.class_def = f'class TimerChannel(ABC):'
    new_class.doc = doc
    shed.pyi.classes.append(new_class)
    shed.def_(
        old='.. method:: timerchannel.callback(fun)',
        new='''
@abstractmethod
def callback(self, fun: Optional[Callable[[Timer], None]], /) -> None
''',
    )
    shed.def_(
        old='.. method:: timerchannel.capture([value])',
        new=['''
@abstractmethod
def capture(self) -> int
''', '''
@abstractmethod
def capture(self, value: int, /) -> None
'''],
    )
    shed.def_(
        old='.. method:: timerchannel.compare([value])',
        new=['''
@abstractmethod
def compare(self) -> int
''', '''
@abstractmethod
def compare(self, value: int, /) -> None
'''],
    )
    shed.def_(
        old='.. method:: timerchannel.pulse_width([value])',
        new=['''
@abstractmethod
def pulse_width(self) -> int
''', '''
@abstractmethod
def pulse_width(self, value: int, /) -> None
'''],
    )
    shed.def_(
        old='.. method:: timerchannel.pulse_width_percent([value])',
        new=['''
@abstractmethod
def pulse_width_percent(self) -> float
''', '''
@abstractmethod
def pulse_width_percent(self, value: Union[int, float], /) -> None
'''],
        end=end,
    )


def _timer(this: str, shed: RST2PyI) -> str:
    shed.class_from_file(
        pre_str='# noinspection PyShadowingNames',
        old=this,
        post_doc='''

   UP: ClassVar[int] = ...
   """
   configures the timer to count from 0 to ARR (default).
   """
   
   DOWN: ClassVar[int] = ...
   """
   configures the timer to count from ARR down to 0.
   """
   
   CENTER: ClassVar[int] = ...
   """
   configures the timer to count from 0 to ARR and then back down to 0.
   """


   PWM: ClassVar[int] = ...
   """
   configure the timer in PWM mode (active high).
   """

   PWM_INVERTED: ClassVar[int] = ...
   """
   configure the timer in PWM mode (active low).
   """
   
   
   OC_TIMING: ClassVar[int] = ...
   """
   indicates that no pin is driven.
   """
   
   OC_ACTIVE: ClassVar[int] = ...
   """
   the pin will be made active when a compare match occurs (active is determined by polarity).
   """
   
   OC_INACTIVE: ClassVar[int] = ...
   """
   the pin will be made inactive when a compare match occurs.
   """
   
   OC_TOGGLE: ClassVar[int] = ...
   """
   the pin will be toggled when an compare match occurs.
   """
   
   OC_FORCED_ACTIVE: ClassVar[int] = ...
   """
   the pin is forced active (compare match is ignored).
   """
   
   OC_FORCED_INACTIVE: ClassVar[int] = ...
   """
   the pin is forced inactive (compare match is ignored).
   """
   
   
   IC: ClassVar[int] = ...
   """
   configure the timer in Input Capture mode.
   """
   
   
   ENC_A: ClassVar[int] = ...
   """
   configure the timer in Encoder mode. The counter only changes when CH1 changes.
   """
   
   ENC_B: ClassVar[int] = ...
   """
   configure the timer in Encoder mode. The counter only changes when CH2 changes.
   """
   
   ENC_AB: ClassVar[int] = ...
   """
   configure the timer in Encoder mode. The counter changes when CH1 or CH2 changes.
   """
   
   
   HIGH: ClassVar[int] = ...
   """
   output is active high.
   """
   
   LOW: ClassVar[int] = ...
   """
   output is active low.
   """
   
   
   RISING: ClassVar[int] = ...
   """
   captures on rising edge.
   """
   
   FALLING: ClassVar[int] = ...
   """
   captures on falling edge.
   """
   
   BOTH: ClassVar[int] = ...
   """
   captures on both edges.
   """
'''
    )
    shed.def_(
        old=r'.. class:: pyb.Timer(id, ...)',
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
   freq: int, 
   mode: int = UP, 
   div: int = 1, 
   callback: Optional[Callable[["Timer"], None]] = None, 
   deadtime: int = 0
)
''', '''
def __init__(
   self, 
   id: int, 
   /, 
   *, 
   prescaler: int, 
   period: int, 
   mode: int = UP, 
   div: int = 1, 
   callback: Optional[Callable[["Timer"], None]] = None, 
   deadtime: int = 0
)
'''],
    )
    shed.def_(
        old=r'.. method:: Timer.init(*, freq, prescaler, period, mode=Timer.UP, div=1, callback=None, deadtime=0)',
        new=['''
def init(
   self, 
   *, 
   freq: int, 
   mode: int = UP, 
   div: int = 1, 
   callback: Optional[Callable[["Timer"], None]] = None, 
   deadtime: int = 0
) -> None
''', '''
def init(
   self, 
   *, 
   prescaler: int, 
   period: int, 
   mode: int = UP, 
   div: int = 1, 
   callback: Optional[Callable[["Timer"], None]] = None, 
   deadtime: int = 0
) -> None
'''],
    )
    shed.def_(
        old=r'.. method:: Timer.deinit()',
        new='def deinit(self) -> None',
    )
    shed.def_(
        old=r'.. method:: Timer.callback(fun)',
        new='def callback(self, fun: Optional[Callable[["Timer"], None]], /) -> None',
    )
    shed.def_(
        old=r'.. method:: Timer.channel(channel, mode, ...)',
        new=['''
def channel(
   self, 
   channel: int, 
   /
) -> Optional["TimerChannel"]
''', '''
def channel(
   self, 
   channel: int, 
   /, 
   mode: int, 
   *, 
   callback: Optional[Callable[["Timer"], None]] = None, 
   pin: Optional[Pin] = None,
   pulse_width: int,
) -> "TimerChannel"
''', '''
def channel(
   self, 
   channel: int, 
   /, 
   mode: int, 
   *, 
   callback: Optional[Callable[["Timer"], None]] = None, 
   pin: Optional[Pin] = None,
   pulse_width_percent: Union[int, float],
) -> "TimerChannel"
''', '''
def channel(
   self, 
   channel: int, 
   /, 
   mode: int, 
   *, 
   callback: Optional[Callable[["Timer"], None]] = None, 
   pin: Optional[Pin] = None,
   compare: int,
   polarity: int,
) -> "TimerChannel"
''', '''
def channel(
   self, 
   channel: int, 
   /, 
   mode: int, 
   *, 
   callback: Optional[Callable[["Timer"], None]] = None, 
   pin: Optional[Pin] = None,
   polarity: int,
) -> "TimerChannel"
''', '''
def channel(
   self, 
   channel: int, 
   /, 
   mode: int, 
   *, 
   callback: Optional[Callable[["Timer"], None]] = None, 
   pin: Optional[Pin] = None,
) -> "TimerChannel"
'''],
    )
    shed.def_(
        old='.. method:: Timer.counter([value])',
        new=[
            'def counter(self) -> int',
            'def counter(self, value: int, /) -> None'
        ],
    )
    shed.def_(
        old='.. method:: Timer.freq([value])',
        new=[
            'def freq(self) -> int',
            'def freq(self, value: int, /) -> None'
        ],
    )
    shed.def_(
        old='.. method:: Timer.period([value])',
        new=[
            'def period(self) -> int',
            'def period(self, value: int, /) -> None'
        ],
    )
    shed.def_(
        old='.. method:: Timer.prescaler([value])',
        new=[
            'def prescaler(self) -> int',
            'def prescaler(self, value: int, /) -> None'
        ],
    )
    timer_channel = 'class TimerChannel --- setup a channel for a timer'
    shed.def_(
        old=r'.. method:: Timer.source_freq()',
        new='def source_freq(self) -> int',
        end=timer_channel,
    )
    nxt = 'pyb.UART.rst'
    _timer_channel(old=timer_channel, end=nxt, shed=shed)
    return nxt


def _switch(this: str, shed: RST2PyI) -> str:
    shed.class_from_file(old=this)
    shed.def_(
        old=r'.. class:: pyb.Switch()',
        new='def __init__(self)',
    )
    shed.def_(
        old=r'.. method:: Switch.__call__()',
        new='def __call__(self) -> bool',
    )
    shed.def_(
        old=r'.. method:: Switch.value()',
        new='def value(self) -> bool',
    )
    nxt = 'pyb.Timer.rst'
    shed.def_(
        old=r'.. method:: Switch.callback(fun)',
        new='def callback(self, fun: Optional[Callable[[], None]]) -> None',
        end=nxt
    )
    return nxt


def _spi(this: str, shed: RST2PyI) -> str:
    shed.class_from_file(old=this)
    shed.def_(
        old='.. class:: pyb.SPI(bus, ...)',
        new=['''
def __init__(self, bus: int, /)
''', '''
def __init__(
   self, 
   bus: int, 
   /, 
   mode: int = MASTER, 
   baudrate: int = 328125, 
   *,
   polarity: int = 1, 
   phase: int = 0, 
   bits: int = 8, 
   firstbit: int = MSB, 
   ti: bool = False, 
   crc: Optional[int] = None
)
''', '''
def __init__(
   self, 
   bus: int, 
   /, 
   mode: int = MASTER, 
   *,
   prescaler: int = 256, 
   polarity: int = 1, 
   phase: int = 0, 
   bits: int = 8, 
   firstbit: int = MSB, 
   ti: bool = False, 
   crc: Optional[int] = None
)
'''],
    )
    shed.def_(
        old=r'.. method:: SPI.deinit()',
        new='def deinit(self) -> None',
    )
    shed.def_(
        old=(
            r'.. method:: SPI.init(mode, baudrate=328125, *, prescaler, '
            r'polarity=1, phase=0, bits=8, firstbit=SPI.MSB, ti=False, crc=None)'
        ),
        new=['''
def init(
   self, 
   mode: int = MASTER, 
   baudrate: int = 328125, 
   *,
   polarity: int = 1, 
   phase: int = 0, 
   bits: int = 8, 
   firstbit: int = MSB, 
   ti: bool = False, 
   crc: Optional[int] = None
)
''', '''
def init(
   self, 
   mode: int = MASTER, 
   *,
   prescaler: int = 256, 
   polarity: int = 1, 
   phase: int = 0, 
   bits: int = 8, 
   firstbit: int = MSB, 
   ti: bool = False, 
   crc: Optional[int] = None
)
'''],
    )
    shed.def_(
        old=r'.. method:: SPI.recv(recv, *, timeout=5000)',
        new='def recv(self, recv: Union[int, _AnyWritableBuf], /, *, timeout: int = 5000) -> _AnyWritableBuf',
    )
    shed.def_(
        old=r'.. method:: SPI.send(send, *, timeout=5000)',
        new='def send(self, send: Union[int, _AnyWritableBuf, bytes], /, *, timeout: int = 5000) -> None',
    )
    shed.def_(
        old=r'.. method:: SPI.send_recv(send, recv=None, *, timeout=5000)',
        new='''
def send_recv(
   self, 
   send: Union[int, bytearray, array, bytes], 
   recv: Optional[_AnyWritableBuf] = None, 
   /, 
   *, 
   timeout: int = 5000
) -> _AnyWritableBuf
''',
    )
    nxt = 'pyb.Switch.rst'
    shed.vars(end=nxt)
    return nxt


def _servo(this: str, shed: RST2PyI) -> str:
    shed.class_from_file(old=this)
    shed.def_(
        old='.. class:: pyb.Servo(id)',
        new='def __init__(self, id: int, /)',
    )
    shed.def_(
        old='.. method:: Servo.angle([angle, time=0])',
        new=[
            'def angle(self) -> int',
            'def angle(self, angle: int, time: int = 0, /) -> None'
        ],
    )
    shed.def_(
        old='.. method:: Servo.speed([speed, time=0])',
        new=[
            'def speed(self) -> int',
            'def speed(self, speed: int, time: int = 0, /) -> None'
        ],
    )
    shed.def_(
        old='.. method:: Servo.pulse_width([value])',
        new=[
            'def speed(self) -> int',
            'def speed(self, value: int, /) -> None'
        ],
    )
    nxt = 'pyb.SPI.rst'
    shed.def_(
        old='.. method:: Servo.calibration([pulse_min, pulse_max, pulse_centre, [pulse_angle_90, pulse_speed_100]])',
        new=['''
def calibration(
   self
) -> Tuple[int, int, int, int, int]
''', '''
def calibration(
   self, 
   pulse_min: int, 
   pulse_max: int, 
   pulse_centre: int, 
   /
) -> None
''', '''
def calibration(
   self, 
   pulse_min: int, 
   pulse_max: int, 
   pulse_centre: int, 
   pulse_angle_90: int, 
   pulse_speed_100: int, 
   /
) -> None
'''],
        end=nxt
    )
    return nxt


def _rtc(this: str, shed: RST2PyI) -> str:
    shed.class_from_file(old=this)
    shed.def_(
        old='.. class:: pyb.RTC()',
        new='def __init__(self)',
    )
    shed.def_(
        old='.. method:: RTC.datetime([datetimetuple])',
        new='def datetime(self, datetimetuple: Tuple[int, int, int, int, int, int, int, int], /) -> None',
    )
    shed.def_(
        old='.. method:: RTC.wakeup(timeout, callback=None)',
        new='def wakeup(self, timeout: Optional[Callable[["RTC"], None]] = None, /) -> None',
    )
    shed.def_(
        old='.. method:: RTC.info()',
        new='def info(self) -> int',
    )
    nxt = 'pyb.Servo.rst'
    shed.def_(
        old='.. method:: RTC.calibration(cal)',
        new=[
            'def calibration(self) -> int',
            'def calibration(self, cal: int, /) -> None'
        ],
        end=nxt
    )
    return nxt


def _pin_af(*, end: str, shed: RST2PyI) -> None:
    shed.consume_name_line('class PinAF -- Pin Alternate Functions')
    shed.consume_title_line()
    shed.consume_blank_line()
    doc = []
    for doc_line in shed.rst:
        if doc_line.startswith('Methods'):
            shed.consume_header_line()
            shed.consume_blank_line()
            break
        doc.append(f'   {doc_line}\n')
    else:
        assert False, f'Expected `{end}`, but did not find it!'
    new_class = Class()
    shed.pyi.classes.append(new_class)
    new_class.class_def = 'class PinAF(ABC):'
    new_class.doc = doc
    new_class.imports_vars.append('   __slots__ = ()')
    shed.def_(
        old='.. method:: pinaf.__str__()',
        new='''
@abstractmethod
def __str__(self) -> str
''',
    )
    shed.def_(
        old='.. method:: pinaf.index()',
        new='''
@abstractmethod
def index(self) -> int
''',
    )
    shed.def_(
        old='.. method:: pinaf.name()',
        new='''
@abstractmethod
def name(self) -> str
''',
    )
    shed.def_(
        old='.. method:: pinaf.reg()',
        new='''
@abstractmethod
def reg(self) -> int
''',
        end=end
    )


def _pin(this: str, shed: RST2PyI) -> str:
    shed.class_from_file(
        pre_str='# noinspection PyNestedDecorators',
        old=this,
        post_doc='''
   
   AF1_TIM1: ClassVar["PinAF"] = ...
   """
   Alternate def_ 1, timer 1.
   """
   
   AF1_TIM2: ClassVar["PinAF"] = ...
   """
   Alternate def_ 1, timer 2.
   """

   AF2_TIM3: ClassVar["PinAF"] = ...
   """
   Alternate def_ 2, timer 3.
   """

   AF2_TIM4: ClassVar["PinAF"] = ...
   """
   Alternate def_ 2, timer 4.
   """

   AF2_TIM5: ClassVar["PinAF"] = ...
   """
   Alternate def_ 2, timer 5.
   """

   AF3_TIM10: ClassVar["PinAF"] = ...
   """
   Alternate def_ 3, timer 10.
   """

   AF3_TIM11: ClassVar["PinAF"] = ...
   """
   Alternate def_ 3, timer 11.
   """

   AF3_TIM8: ClassVar["PinAF"] = ...
   """
   Alternate def_ 3, timer 8.
   """

   AF3_TIM9: ClassVar["PinAF"] = ...
   """
   Alternate def_ 3, timer 9.
   """

   AF4_I2C1: ClassVar["PinAF"] = ...
   """
   Alternate def_ 4, I2C 1.
   """

   AF4_I2C2: ClassVar["PinAF"] = ...
   """
   Alternate def_ 4, I2C 2.
   """

   AF5_SPI1: ClassVar["PinAF"] = ...
   """
   Alternate def_ 5, SPI 1.
   """

   AF5_SPI2: ClassVar["PinAF"] = ...
   """
   Alternate def_ 5, SPI 2.
   """

   AF7_USART1: ClassVar["PinAF"] = ...
   """
   Alternate def_ 7, USART 1.
   """

   AF7_USART2: ClassVar["PinAF"] = ...
   """
   Alternate def_ 7, USART 2.
   """

   AF7_USART3: ClassVar["PinAF"] = ...
   """
   Alternate def_ 7, USART 3.
   """

   AF8_UART4: ClassVar["PinAF"] = ...
   """
   Alternate def_ 8, USART 4.
   """

   AF8_USART6: ClassVar["PinAF"] = ...
   """
   Alternate def_ 8, USART 6.
   """

   AF9_CAN1: ClassVar["PinAF"] = ...
   """
   Alternate def_ 9, CAN 1.
   """

   AF9_CAN2: ClassVar["PinAF"] = ...
   """
   Alternate def_ 9, CAN 2.
   """

   AF9_TIM12: ClassVar["PinAF"] = ...
   """
   Alternate def_ 9, timer 12.
   """

   AF9_TIM13: ClassVar["PinAF"] = ...
   """
   Alternate def_ 9, timer 13.
   """

   AF9_TIM14: ClassVar["PinAF"] = ...
   """
   Alternate def_ 9, timer 14.
   """


   ALT: ClassVar[int] = ...
   """
   Initialise the pin to alternate-def_ mode with a push-pull drive (same as `AF_PP`).
   """

   ALT_OPEN_DRAIN: ClassVar[int] = ...
   """
   Initialise the pin to alternate-def_ mode with an open-drain drive (same as `AF_OD`).
   """

   IRQ_FALLING: ClassVar[int] = ...
   """
   Initialise the pin to generate an interrupt on a falling edge.
   """

   IRQ_RISING: ClassVar[int] = ...
   """
   Initialise the pin to generate an interrupt on a rising edge.
   """

   OPEN_DRAIN: ClassVar[int] = ...
   """
   Initialise the pin to output mode with an open-drain drive (same as `OUT_OD`).
   """
   
   
   class board:
      """
      The board pins (board nomenclature, e.g. `X1`) that are bought out onto pads on a PyBoard.
      """

      LED_BLUE: ClassVar["Pin"] = ...
      """
      The blue LED.
      """
      
      LED_GREEN: ClassVar["Pin"] = ...
      """
      The green LED.
      """
      
      LED_RED: ClassVar["Pin"] = ...
      """
      The red LED.
      """
      
      LED_YELLOW: ClassVar["Pin"] = ...
      """
      The yellow LED.
      """
      
      MMA_AVDD: ClassVar["Pin"] = ...
      """
      Accelerometer (MMA7660) analogue power (AVDD) pin.
      """
      
      MMA_INT: ClassVar["Pin"] = ...
      """
      Accelerometer (MMA7660) interrupt (\\INT) pin.
      """
      
      SD: ClassVar["Pin"] = ...
      """
      SD card present switch (0 for card inserted, 1 for no card) (same as SD_SW).
      """

      SD_CK: ClassVar["Pin"] = ...
      """
      SD card clock.
      """

      SD_CMD: ClassVar["Pin"] = ...
      """
      SD card command.
      """

      SD_D0: ClassVar["Pin"] = ...
      """
      SD card serial data 0.
      """

      SD_D1: ClassVar["Pin"] = ...
      """
      SD card serial data 1.
      """

      SD_D2: ClassVar["Pin"] = ...
      """
      SD card serial data 2.
      """

      SD_D3: ClassVar["Pin"] = ...
      """
      SD card serial data 3.
      """

      SD_SW: ClassVar["Pin"] = ...
      """
      SD card present switch (0 for card inserted, 1 for no card) (same as SD).
      """

      SW: ClassVar["Pin"] = ...
      """
      Usr switch (0 = pressed, 1 = not pressed).
      """

      USB_DM: ClassVar["Pin"] = ...
      """
      USB data -.
      """

      USB_DP: ClassVar["Pin"] = ...
      """
      USB data +.
      """

      USB_ID: ClassVar["Pin"] = ...
      """
      USB OTG (on-the-go) ID.
      """

      USB_VBUS: ClassVar["Pin"] = ...
      """
      USB VBUS (power) monitoring pin.
      """

      X1: ClassVar["Pin"] = ...
      """
      X1 pin.
      """

      X10: ClassVar["Pin"] = ...
      """
      X10 pin.
      """

      X11: ClassVar["Pin"] = ...
      """
      X11 pin.
      """

      X12: ClassVar["Pin"] = ...
      """
      X12 pin.
      """

      X17: ClassVar["Pin"] = ...
      """
      X17 pin.
      """

      X18: ClassVar["Pin"] = ...
      """
      X18 pin.
      """

      X19: ClassVar["Pin"] = ...
      """
      X19 pin.
      """

      X2: ClassVar["Pin"] = ...
      """
      X2 pin.
      """

      X20: ClassVar["Pin"] = ...
      """
      X20 pin.
      """

      X21: ClassVar["Pin"] = ...
      """
      X21 pin.
      """
             
      X22: ClassVar["Pin"] = ...
      """
      X22 pin.
      """

      X3: ClassVar["Pin"] = ...
      """
      X3 pin.
      """

      X4: ClassVar["Pin"] = ...
      """
      X4 pin.
      """

      X5: ClassVar["Pin"] = ...
      """
      X5 pin.
      """

      X6: ClassVar["Pin"] = ...
      """
      X6 pin.
      """

      X7: ClassVar["Pin"] = ...
      """
      X7 pin.
      """

      X8: ClassVar["Pin"] = ...
      """
      X8 pin.
      """

      X9: ClassVar["Pin"] = ...
      """
      X9 pin.
      """

      Y1: ClassVar["Pin"] = ...
      """
      Y1 pin.
      """

      Y10: ClassVar["Pin"] = ...
      """
      Y10 pin.
      """

      Y11: ClassVar["Pin"] = ...
      """
      Y11 pin.
      """

      Y12: ClassVar["Pin"] = ...
      """
      Y12 pin.
      """

      Y2: ClassVar["Pin"] = ...
      """
      Y2 pin.
      """

      Y3: ClassVar["Pin"] = ...
      """
      Y3 pin.
      """

      Y4: ClassVar["Pin"] = ...
      """
      Y4 pin.
      """

      Y5: ClassVar["Pin"] = ...
      """
      Y5 pin.
      """

      Y6: ClassVar["Pin"] = ...
      """
      Y6 pin.
      """

      Y7: ClassVar["Pin"] = ...
      """
      Y7 pin.
      """

      Y8: ClassVar["Pin"] = ...
      """
      Y8 pin.
      """

      Y9: ClassVar["Pin"] = ...
      """
      Y9 pin.
      """
   
   
   class cpu:
      """
      The CPU pins (CPU nomenclature, e.g. `A0`) that are bought out onto pads on a PyBoard.
      """
      
      A0: ClassVar["Pin"] = ...
      """
      A0 pin.
      """
      
      A1: ClassVar["Pin"] = ...
      """
      A1 pin.
      """

      A10: ClassVar["Pin"] = ...
      """
      A10 pin.
      """

      A11: ClassVar["Pin"] = ...
      """
      A11 pin.
      """

      A12: ClassVar["Pin"] = ...
      """
      A12 pin.
      """

      A13: ClassVar["Pin"] = ...
      """
      A13 pin.
      """

      A14: ClassVar["Pin"] = ...
      """
      A14 pin.
      """

      A15: ClassVar["Pin"] = ...
      """
      A15 pin.
      """

      A2: ClassVar["Pin"] = ...
      """
      A2 pin.
      """

      A3: ClassVar["Pin"] = ...
      """
      A3 pin.
      """

      A4: ClassVar["Pin"] = ...
      """
      A4 pin.
      """

      A5: ClassVar["Pin"] = ...
      """
      A5 pin.
      """

      A6: ClassVar["Pin"] = ...
      """
      A6 pin.
      """

      A7: ClassVar["Pin"] = ...
      """
      A7 pin.
      """

      A8: ClassVar["Pin"] = ...
      """
      A8 pin.
      """

      A9: ClassVar["Pin"] = ...
      """
      A9 pin.
      """

      B0: ClassVar["Pin"] = ...
      """
      B0 pin.
      """

      B1: ClassVar["Pin"] = ...
      """
      B1 pin.
      """

      B10: ClassVar["Pin"] = ...
      """
      B10 pin.
      """

      B11: ClassVar["Pin"] = ...
      """
      B11 pin.
      """

      B12: ClassVar["Pin"] = ...
      """
      B12 pin.
      """

      B13: ClassVar["Pin"] = ...
      """
      B13 pin.
      """

      B14: ClassVar["Pin"] = ...
      """
      B14 pin.
      """

      B15: ClassVar["Pin"] = ...
      """
      B15 pin.
      """

      B2: ClassVar["Pin"] = ...
      """
      B2 pin.
      """

      B3: ClassVar["Pin"] = ...
      """
      B3 pin.
      """

      B4: ClassVar["Pin"] = ...
      """
      B4 pin.
      """

      B5: ClassVar["Pin"] = ...
      """
      B5 pin.
      """

      B6: ClassVar["Pin"] = ...
      """
      B6 pin.
      """

      B7: ClassVar["Pin"] = ...
      """
      B7 pin.
      """

      B8: ClassVar["Pin"] = ...
      """
      B8 pin.
      """

      B9: ClassVar["Pin"] = ...
      """
      B9 pin.
      """

      C0: ClassVar["Pin"] = ...
      """
      C0 pin.
      """

      C1: ClassVar["Pin"] = ...
      """
      C1 pin.
      """

      C10: ClassVar["Pin"] = ...
      """
      C10 pin.
      """

      C11: ClassVar["Pin"] = ...
      """
      C11 pin.
      """

      C12: ClassVar["Pin"] = ...
      """
      C12 pin.
      """

      C13: ClassVar["Pin"] = ...
      """
      C13 pin.
      """

      C2: ClassVar["Pin"] = ...
      """
      C2 pin.
      """

      C3: ClassVar["Pin"] = ...
      """
      C3 pin.
      """

      C4: ClassVar["Pin"] = ...
      """
      C4 pin.
      """

      C5: ClassVar["Pin"] = ...
      """
      C5 pin.
      """

      C6: ClassVar["Pin"] = ...
      """
      C6 pin.
      """

      C7: ClassVar["Pin"] = ...
      """
      C7 pin.
      """

      C8: ClassVar["Pin"] = ...
      """
      C8 pin.
      """

      C9: ClassVar["Pin"] = ...
      """
      C9 pin.
      """

      D2: ClassVar["Pin"] = ...
      """
      D2 pin.
      """
''')
    shed.def_(
        old='.. class:: pyb.Pin(id, ...)',
        new='''
def __init__(self, id: Union["Pin", str], /, mode: int = IN, pull: int = PULL_NONE, af: Union[str, int] = -1)
''',
    )
    shed.def_(
        old='.. classmethod:: Pin.debug([state])',
        new=['''
@staticmethod
def debug() -> bool
''', '''
@staticmethod
def debug(state: bool, /) -> None
'''],
    )
    shed.def_(
        old='.. classmethod:: Pin.dict([dict])',
        new=['''
@staticmethod
def dict() -> Dict[str, "Pin"]
''', '''
@staticmethod
def dict(dict: Dict[str, "Pin"], /) -> None
'''],
    )
    shed.def_(
        old='.. classmethod:: Pin.mapper([fun])',
        new=['''
@staticmethod
def mapper() -> Callable[[str], "Pin"]
''', '''
@staticmethod
def mapper(fun: Callable[[str], "Pin"], /) -> None
'''],
    )
    shed.def_(
        old='.. method:: Pin.init(mode, pull=Pin.PULL_NONE, af=-1)',
        new='def init(self, mode: int = IN, pull: int = PULL_NONE, af: Union[str, int] = -1) -> None',
    )
    shed.def_(
        old='.. method:: Pin.value([value])',
        new=[
            'def value(self) -> int',
            'def value(self, value: Any, /) -> None'
        ],
    )
    shed.def_(
        old='.. method:: Pin.__str__()',
        new='def __str__(self) -> str',
    )
    shed.def_(
        old='.. method:: Pin.af()',
        new='def af(self) -> int',
    )
    shed.def_(
        old='.. method:: Pin.af_list()',
        new='def af_list(self) -> List["PinAF"]',
    )
    shed.def_(
        old='.. method:: Pin.gpio()',
        new='def gpio(self) -> int',
    )
    shed.def_(
        old='.. method:: Pin.mode()',
        new='def mode(self) -> int',
    )
    shed.def_(
        old='.. method:: Pin.name()',
        new='def name(self) -> str',
    )
    shed.def_(
        old='.. method:: Pin.names()',
        new='def names(self) -> List[str]',
    )
    shed.def_(
        old='.. method:: Pin.pin()',
        new='def pin(self) -> int',
    )
    shed.def_(
        old='.. method:: Pin.port()',
        new='def port(self) -> int',
    )
    shed.def_(
        old='.. method:: Pin.pull()',
        new='def pull(self) -> int',
    )
    shed.vars(end='class PinAF -- Pin Alternate Functions')
    nxt = 'pyb.RTC.rst'
    _pin_af(end=nxt, shed=shed)
    return nxt


def _led(this: str, shed: RST2PyI) -> str:
    shed.class_from_file(old=this)
    shed.def_(
        old='.. class:: pyb.LED(id)',
        new='def __init__(self, id: int, /)',
    )
    shed.def_(
        old='.. method:: LED.intensity([value])',
        new=[
            'def intensity(self) -> int',
            'def intensity(self, value: int, /) -> None'
        ],
    )
    shed.def_(
        old='.. method:: LED.off()',
        new='def off(self) -> None',
    )
    shed.def_(
        old='.. method:: LED.on()',
        new='def on(self) -> None',
    )
    nxt = 'pyb.Pin.rst'
    shed.def_(
        old='.. method:: LED.toggle()',
        new='def toggle(self) -> None',
        end=nxt
    )
    return nxt


def _lcd(this: str, shed: RST2PyI) -> str:
    shed.class_from_file(old=this)
    shed.def_(
        old='.. class:: pyb.LCD(skin_position)',
        new='def __init__(self, skin_position: str, /)',
    )
    shed.def_(
        old='.. method:: LCD.command(instr_data, buf)',
        new='def command(self, inst_data: int, buf: bytes, /) -> None',
    )
    shed.def_(
        old='.. method:: LCD.contrast(value)',
        new='def contrast(self, value: int, /) -> None',
    )
    shed.def_(
        old='.. method:: LCD.fill(colour)',
        new='def fill(self, colour: int, /) -> None',
    )
    shed.def_(
        old='.. method:: LCD.get(x, y)',
        new='def get(self, x: int, y: int, /) -> int',
    )
    shed.def_(
        old='.. method:: LCD.light(value)',
        new='def light(self, value: Union[bool, int], /) -> None',
    )
    shed.def_(
        old='.. method:: LCD.pixel(x, y, colour)',
        new='def pixel(self, x: int, y: int, colour: int, /) -> None',
    )
    shed.def_(
        old='.. method:: LCD.show()',
        new='def show(self) -> None',
    )
    shed.def_(
        old='.. method:: LCD.text(str, x, y, colour)',
        new='def text(self, str: str, x: int, y: int, colour: int, /) -> None',
    )
    nxt = 'pyb.LED.rst'
    shed.def_(
        old='.. method:: LCD.write(str)',
        new='def write(self, str: str, /) -> None',
        end=nxt
    )
    return nxt


def _i2c(this: str, shed: RST2PyI) -> str:
    shed.class_from_file(old=this, )
    shed.def_(
        old=r'.. class:: pyb.I2C(bus, ...)',
        new='''
def __init__(
   self, 
   bus: Union[int, str], 
   mode: str, 
   /, 
   *, 
   addr: int = 0x12, 
   baudrate: int = 400_000, 
   gencall: bool = False, 
   dma: bool = False
)
''',
    )
    shed.def_(
        old=r'.. method:: I2C.deinit()',
        new='def deinit(self) -> None',
    )
    shed.def_(
        old=r'.. method:: I2C.init(mode, *, addr=0x12, baudrate=400000, gencall=False, dma=False)',
        new='''
def init(
   self, 
   bus: Union[int, str], 
   mode: str, 
   /, 
   *, 
   addr: int = 0x12, 
   baudrate: int = 400_000, 
   gencall: bool = False, 
   dma: bool = False
) -> None
''',
    )
    shed.def_(
        old=r'.. method:: I2C.is_ready(addr)',
        new='def is_ready(self, addr: int, /) -> bool',
    )
    shed.def_(
        old=r'.. method:: I2C.mem_read(data, addr, memaddr, *, timeout=5000, addr_size=8)',
        new='''
def mem_read(
   self, 
   data: Union[int, _AnyWritableBuf], 
   addr: int, 
   memaddr: int,
   /, 
   *, 
   timeout: int = 5000, 
   addr_size: int = 8, 
) -> bytes
''',
    )
    return 'pyb.LCD.rst'


def _flash(this: str, shed: RST2PyI) -> str:
    shed.class_from_file(old=this, )
    shed.def_(
        old='.. class:: pyb.Flash()',
        new='''
@overload
def __init__(self)
''',
    )
    shed.def_(
        old=r'.. class:: pyb.Flash(*, start=-1, len=-1)',
        new='''
@overload
def __init__(self, *, start: int = -1, len: int = -1)
''',
    )
    shed.defs_with_common_description(
        cmd='.. method:: Flash.',  # Needs `.` at end!
        old2new={
            'readblocks(block_num, buf)':
                'def readblocks(self, blocknum: int, buf: bytes, offset: int = 0, /) -> None',
            'readblocks(block_num, buf, offset)':
                '',
            'writeblocks(block_num, buf)':
                'def writeblocks(self, blocknum: int, buf: bytes, offset: int = 0, /) -> None',
            'writeblocks(block_num, buf, offset)':
                '',
            'ioctl(cmd, arg)':
                'def ioctl(self, op: int, arg: int) -> Optional[int]',
        },
        end='Hardware Note'
    )
    nxt = 'pyb.I2C.rst'
    shed.pyi.doc += shed.extra_notes(end=nxt)
    return nxt


def _ext_int(this: str, shed: RST2PyI) -> str:
    shed.class_from_file(old=this, )
    shed.def_(
        old='.. class:: pyb.ExtInt(pin, mode, pull, callback)',
        new='def __init__(self, pin: Union[int, str, "Pin"], mode: int, pull: int, callback: Callable[[int], None])',
    )
    shed.def_(
        old='.. classmethod:: ExtInt.regs()',
        new='''
@staticmethod
def regs() -> None
''',
    )
    shed.def_(
        old='.. method:: ExtInt.disable()',
        new='def disable(self) -> None',
    )
    shed.def_(
        old='.. method:: ExtInt.enable()',
        new='def enable(self) -> None',
    )
    shed.def_(
        old='.. method:: ExtInt.line()',
        new='def line(self) -> int',
    )
    shed.def_(
        old='.. method:: ExtInt.swint()',
        new='def swint(self) -> None',
    )
    nxt = 'pyb.Flash.rst'
    shed.vars(end=nxt)
    return nxt


def _dac(this: str, shed: RST2PyI) -> str:
    shed.class_from_file(
        pre_str='# noinspection PyShadowingNames',
        old=this,
        post_doc='''
      
   NORMAL: ClassVar[int] = ...
   """
   Normal mode (output buffer once) for `mode` argument of `write_timed`.
   """
   
   CIRCULAR: ClassVar[int] = ...
   """
   Circular mode (output buffer continuously) for `mode` argument of `write_timed`.
   """
''',
    )
    shed.def_(
        old=r'.. class:: pyb.DAC(port, bits=8, *, buffering=None)',
        new='def __init__(self, port: Union[int, "Pin"], /, bits: int = 8, *, buffering: Optional[bool] = None)',
    )
    shed.def_(
        old=r'.. method:: DAC.init(bits=8, *, buffering=None)',
        new='def init(self, bits: int = 8, *, buffering: Optional[bool] = None) -> None',
    )
    shed.def_(
        old='.. method:: DAC.deinit()',
        new='def deinit(self) -> None',
    )
    shed.def_(
        old='.. method:: DAC.noise(freq)',
        new='def noise(self, freq: int, /) -> None',
    )
    shed.def_(
        old='.. method:: DAC.triangle(freq)',
        new='def triangle(self, freq: int, /) -> None',
    )
    shed.def_(
        old='.. method:: DAC.write(value)',
        new='def write(self, value: int, /) -> None',
    )
    nxt = 'pyb.ExtInt.rst'
    shed.def_(
        old=r'.. method:: DAC.write_timed(data, freq, *, mode=DAC.NORMAL)',
        new='def write_timed(self, data: _AnyWritableBuf, freq: Union[int, "Timer"], /, *, mode: int = NORMAL) -> None',
        end=nxt,
    )
    return nxt


def _can(this: str, shed: RST2PyI) -> str:
    shed.class_from_file(old=this, )
    shed.def_(
        old='.. class:: pyb.CAN(bus, ...)',
        new='''
def __init__(
   self, 
   bus: Union[int, str], 
   mode: int,
   /,
   extframe: bool = False, 
   prescaler: int = 100, 
   *, 
   sjw: int = 1, 
   bs1: int = 6, 
   bs2: int = 8, 
   auto_restart: bool = False
)
''',
    )
    shed.def_(
        old='.. classmethod:: CAN.initfilterbanks(nr)',
        new='''
@staticmethod
def initfilterbanks(nr: int, /) -> None
''',
    )
    shed.def_(
        old=(
            r'.. method:: CAN.init(mode, extframe=False, prescaler=100, *, sjw=1, bs1=6, '
            r'bs2=8, auto_restart=False, baudrate=0, sample_point=75)'
        ),
        new='''
def init(
   self, 
   mode: int,
   /,
   extframe: bool = False   , 
   prescaler: int = 100, 
   *, 
   sjw: int = 1, 
   bs1: int = 6, 
   bs2: int = 8, 
   auto_restart: bool = False,
   baudrate: int = 0,
   sample_point: int = 75
) -> None
''',
    )
    shed.def_(
        old='.. method:: CAN.deinit()',
        new='def deinit(self) -> None',
    )
    shed.def_(
        old='.. method:: CAN.restart()',
        new='def restart(self) -> None',
    )
    shed.def_(
        old='.. method:: CAN.state()',
        new='def state(self) -> int',
    )
    shed.def_(
        old='.. method:: CAN.info([list])',
        new=[
            'def info(self) -> List[int]',
            'def info(self, list: List[int], /) -> List[int]'
        ],
    )
    shed.def_(
        old=r'.. method:: CAN.setfilter(bank, mode, fifo, params, *, rtr)',
        new=['''
def setfilter(self, bank: int, mode: int, fifo: int, params: Sequence[int], /) -> None
''', '''
def setfilter(
   self, 
   bank: int, 
   mode: int, 
   fifo: int, 
   params: Sequence[int], 
   /, 
   *, 
   rtr: Sequence[bool]
) -> None
'''],
    )
    shed.def_(
        old='.. method:: CAN.clearfilter(bank)',
        new='def clearfilter(self, bank: int, /) -> None',
    )
    shed.def_(
        old='.. method:: CAN.any(fifo)',
        new='def any(self, fifo: int, /) -> bool',
    )
    shed.def_(
        old=r'.. method:: CAN.recv(fifo, list=None, *, timeout=5000)',
        new=[
            'def recv(self, fifo: int, /, *, timeout: int = 5000) -> Tuple[int, bool, int, memoryview]',
            'def recv(self, fifo: int, list: None, /, *, timeout: int = 5000) -> Tuple[int, bool, int, memoryview]',
            'def recv(self, fifo: int, list: List[Union[int, bool, memoryview]], /, *, timeout: int = 5000) -> None'
        ],
    )
    shed.def_(
        old=r'.. method:: CAN.send(data, id, *, timeout=0, rtr=False)',
        new='''
def send(self, data: Union[int, _AnyWritableBuf], id: int, /, *, timeout: int = 0, rtr: bool = False) -> None
''',
    )
    shed.def_(
        old='.. method:: CAN.rxcallback(fifo, fun)',
        new='def rxcallback(self, fifo: int, fun: Callable[["CAN"], None], /) -> None',
    )
    nxt = 'pyb.DAC.rst'
    shed.vars(end=nxt)
    return nxt


def _adc_all(*, this: str, end: str, shed: RST2PyI) -> None:
    shed.consume_name_line(this)
    shed.consume_header_line()
    shed.consume_blank_line()
    doc = []
    for doc_line in shed.rst:
        if doc_line.lstrip().startswith(end):
            shed.rst.push_line(doc_line)
            break
        doc.append(f'   {doc_line}\n')
    else:
        assert False, f'Did not find: {end}'
    new_class = Class()
    shed.pyi.classes.append(new_class)
    new_class.class_def = 'class ADCAll:'
    new_class.doc = doc
    new_class.defs.append(f'''
   def __init__(self, resolution: int, mask: int = 0xffffffff, /):
      """
      Create a multi-channel ADC instance.

      ``resolution`` is the number of bits for all the ADCs (even those not enabled); one of: 
      14, 12, 10, or 8 bits.

      To avoid unwanted activation of analog inputs (channel 0..15) a second parameter, ``mask``, 
      can be specified.
      This parameter is a binary pattern where each requested analog input has the corresponding bit set.
      The default value is 0xffffffff which means all analog inputs are active. If just the internal
      channels (16..18) are required, the mask value should be 0x70000.
      """

   def read_channel(self, channel: int, /) -> int:
      """
      Read the given channel.
      """

   def read_core_temp(self) -> float:
      """
      Read MCU temperature (centigrade).
      """

   def read_core_vbat(self) -> float:
      """
      Read MCU VBAT (volts).
      """

   def read_core_vref(self) -> float:
      """
      Read MCU VREF (volts).
      """

   def read_vref(self) -> float:
      """
      Read MCU supply voltage (volts).
      """
''')


def _adc(this: str, shed: RST2PyI) -> str:
    shed.class_from_file(old=this)
    shed.def_(
        old='.. class:: pyb.ADC(pin)',
        new='def __init__(self, pin: Union[int, "Pin"], /)',
    )
    shed.def_(
        old='.. method:: ADC.read()',
        new='def read(self) -> int',
    )
    shed.def_(
        old='.. method:: ADC.read_timed(buf, timer)',
        new='def read_timed(self, buf: _AnyWritableBuf, timer: Union["Timer", int], /) -> None',
    )
    extra = 'The ADCAll Object'
    shed.def_(
        old='.. method:: ADC.read_timed_multi((adcx, adcy, ...), (bufx, bufy, ...), timer)',
        new='''
@staticmethod
def read_timed_multi(
   adcs: Tuple['ADC', ...], 
   bufs: Tuple[_AnyWritableBuf, ...], 
   timer: "Timer", 
   /
) -> bool
''',
        end=extra
    )
    nxt = 'pyb.CAN.rst'
    _adc_all(this=extra, end=nxt, shed=shed)
    return nxt


def _accel(shed: RST2PyI) -> str:
    shed.class_from_file(old='pyb.Accel.rst')
    shed.def_(
        old='.. class:: pyb.Accel()',
        new='def __init__(self)',
    )
    shed.def_(
        old='.. method:: Accel.filtered_xyz()',
        new='def filtered_xyz(self) -> Tuple[int, int, int]',
    )
    shed.def_(
        old='.. method:: Accel.tilt()',
        new='def tilt(self) -> int',
    )
    shed.def_(
        old='.. method:: Accel.x()',
        new='def x(self) -> int',
    )
    shed.def_(
        old='.. method:: Accel.y()',
        new='def y(self) -> int',
    )
    shed.def_(
        old='.. method:: Accel.z()',
        new='def z(self) -> int',
        end='Hardware Note'
    )
    nxt = 'pyb.ADC.rst'
    shed.pyi.doc += shed.extra_notes(end=nxt)
    return nxt


def _pyb(shed: RST2PyI) -> None:
    shed.module(
        name='pyb',
        old='functions related to the board',
        post_doc=f'''
from abc import ABC, abstractmethod
from typing import NoReturn, overload, Tuple, Sequence, runtime_checkable, Protocol
from typing import Optional, Union, TypeVar, List, Callable, Dict, Any, ClassVar

from uarray import array


@runtime_checkable
class _OldAbstractReadOnlyBlockDev(Protocol):
    """
    A `Protocol` (structurally typed) with the defs needed by 
    `mount` argument `device` for read-only devices.
    """

    __slots__ = ()

    @abstractmethod
    def readblocks(self, blocknum: int, buf: bytes, /) -> None: ...

    @abstractmethod
    def count(self) -> int: ...


@runtime_checkable
class _OldAbstractBlockDev(_OldAbstractReadOnlyBlockDev, Protocol):
    """
    A `Protocol` (structurally typed) with the defs needed by 
    `mount` argument `device` for read-write devices.
    """

    __slots__ = ()

    @abstractmethod
    def writeblocks(self, blocknum: int, buf: bytes, /) -> None: ...

    @abstractmethod
    def sync(self) -> None: ...


{repdefs.AbstractBlockDev}


hid_mouse: Tuple[int, int, int, int, bytes] = ...
"""
Mouse human interface device (hid), see `hid` argument of `usb_mode`.
"""


hid_keyboard: Tuple[int, int, int, int, bytes] = ...
"""
Keyboard human interface device (hid), see `hid` argument of `usb_mode`.
"""


{repdefs.AnyWritableBuf}


{repdefs.AnyReadableBuf}
''',
    )
    shed.def_(
        old='.. function:: delay(ms)',
        new='def delay(ms: int, /) -> None',
        indent=0
    )
    shed.def_(
        old='.. function:: udelay(us)',
        new='def udelay(us: int, /) -> None',
        indent=0
    )
    shed.def_(
        old='.. function:: millis()',
        new='def millis() -> int',
        indent=0
    )
    shed.def_(
        old='.. function:: micros()',
        new='def micros() -> int',
        indent=0
    )
    shed.def_(
        old='.. function:: elapsed_millis(start)',
        new='def elapsed_millis(start: int, /) -> int',
        indent=0
    )
    shed.def_(
        old='.. function:: elapsed_micros(start)',
        new='def elapsed_micros(start: int, /) -> int',
        indent=0
    )
    shed.def_(
        old='.. function:: hard_reset()',
        new='def hard_reset() -> NoReturn',
        indent=0
    )
    shed.def_(
        old='.. function:: bootloader()',
        new='def bootloader() -> NoReturn',
        indent=0
    )
    shed.def_(
        old='.. function:: fault_debug(value)',
        new='def fault_debug(value: bool = False) -> None',
        indent=0
    )
    shed.def_(
        old='.. function:: disable_irq()',
        new='def disable_irq() -> bool',
        indent=0
    )
    shed.def_(
        old='.. function:: enable_irq(state=True)',
        new='def enable_irq(state: bool = True, /) -> None',
        indent=0
    )
    shed.def_(
        old='.. function:: freq([sysclk[, hclk[, pclk1[, pclk2]]]])',
        new=[
            'def freq() -> Tuple[int, int, int, int]',
            'def freq(sysclk: int, /) -> None',
            'def freq(sysclk: int, hclk: int, /) -> None',
            'def freq(sysclk: int, hclk: int, pclk1: int, /) -> None',
            'def freq(sysclk: int, hclk: int, pclk1: int, pclk2: int, /) -> None'
        ],
        indent=0
    )
    shed.def_(
        old='.. function:: wfi()',
        new='def wfi() -> None',
        indent=0
    )
    shed.def_(
        old='.. function:: stop()',
        new='def stop() -> None',
        indent=0
    )
    shed.def_(
        old='.. function:: standby()',
        new='def standby() -> None',
        indent=0
    )
    shed.def_(
        old='.. function:: have_cdc()',
        new='def have_cdc() -> bool',
        indent=0
    )
    shed.def_(
        old='.. function:: hid((buttons, x, y, z))',
        new=[
            'def hid(data: Tuple[int, int, int, int], /) -> None',
            'def hid(data: Sequence[int], /) -> None'
        ],
        indent=0
    )
    shed.def_(
        old='.. function:: info([dump_alloc_table])',
        new=[
            'def info() -> None',
            'def info(dump_alloc_table: bytes, /) -> None'
        ],
        indent=0
    )
    shed.def_(
        old='.. function:: main(filename)',
        new='def main(filename: str, /) -> None',
        indent=0
    )
    shed.def_(
        old=r'.. function:: mount(device, mountpoint, *, readonly=False, mkfs=False)',
        new=['''
def mount(
   device: _OldAbstractReadOnlyBlockDev, 
   mountpoint: str, 
   /, 
   *, 
   readonly: bool = False, 
   mkfs: bool = False
) -> None
''', '''
def mount(
   device: _OldAbstractBlockDev, 
   mountpoint: str, 
   /, 
   *, 
   readonly: bool = False, 
   mkfs: bool = False
) -> None
'''],
        indent=0
    )
    shed.def_(
        old='.. function:: repl_uart(uart)',
        new=[
            'def repl_uart() -> Optional["UART"]',
            'def repl_uart(uart: "UART", /) -> None'
        ],
        indent=0
    )
    shed.def_(
        old='.. function:: rng()',
        new='def rng() -> int',
        indent=0
    )
    shed.def_(
        old='.. function:: sync()',
        new='def sync() -> None',
        indent=0
    )
    shed.def_(
        old='.. function:: unique_id()',
        new='def unique_id() -> bytes',
        indent=0
    )
    shed.def_(
        pre_str='# noinspection PyShadowingNames',
        old=(
            '.. function:: usb_mode('
            '[modestr], port=-1, vid=0xf055, pid=-1, msc=(), hid=pyb.hid_mouse, high_speed=False)'
        ),
        new=['''
def usb_mode() -> str
''', '''
def usb_mode(
   modestr: str, 
   /, 
   *, 
   port: int = -1, 
   vid: int = 0xf055, 
   pid: int = -1, 
   msc: Sequence[_AbstractBlockDev] = (), 
   hid: Tuple[int, int, int, int, bytes] = hid_mouse, 
   high_speed: bool = False
) -> None
'''],
        indent=0,
        end='Classes'
    )
