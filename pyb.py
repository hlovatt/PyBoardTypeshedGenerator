from typeshed import Typeshed

__author__ = "Howard C Lovatt"
__copyright_ = "Howard C Lovatt, 2020 onwards."
__license__ = "MIT https://opensource.org/licenses/MIT (as used by MicroPython)."
__version__ = "1.0.0"


def pyb(*, output_dir: str):
    shd = _pyb(output_dir=output_dir)
    nxt = _acl(shd)
    nxt = _adc(nxt, shd)
    nxt = _can(nxt, shd)
    nxt = _dac(nxt, shd)
    nxt = _eit(nxt, shd)
    nxt = _flh(nxt, shd)
    nxt = _i2c(nxt, shd)
    nxt = _lcd(nxt, shd)
    nxt = _led(nxt, shd)
    nxt = _pin(nxt, shd)
    nxt = _rtc(nxt, shd)
    nxt = _svo(nxt, shd)
    nxt = _spi(nxt, shd)
    nxt = _swt(nxt, shd)
    nxt = _tim(nxt, shd)
    nxt = _urt(nxt, shd)
    nxt = _uhd(nxt, shd)
    _uvp(nxt, shd)

    shd.write()


def _uvp(this: str, shed: Typeshed):
    shed.class_(old=this)
    shed.def_(
        old=r'.. class:: pyb.USB_VCP(id=0)',
        new='def __init__(self, id: int = 0, /)',
        indent=3,
    )
    shed.def_(
        old=r'.. method:: USB_VCP.init(\*, flow=-1)',
        new='def init(self, *, flow: int = - 1) -> int',
        indent=3,
    )
    shed.def_(
        old=r'.. method:: USB_VCP.setinterrupt(chr)',
        new='def setinterrupt(self, chr: int, /) -> None',
        indent=3,
    )
    shed.def_(
        old=r'.. method:: USB_VCP.isconnected()',
        new='def isconnected(self) -> bool',
        indent=3,
    )
    shed.def_(
        old=r'.. method:: USB_VCP.any()',
        new='def any(self) -> bool',
        indent=3,
    )
    shed.def_(
        old=r'.. method:: USB_VCP.close()',
        new='def close(self) -> None',
        indent=3,
    )
    shed.def_(
        old=r'.. method:: USB_VCP.read([nbytes])',
        new='''
@overload
def read(self) -> Optional[bytes]: ...
@overload
def read(self, nbytes, /) -> Optional[bytes]
''',
        indent=3,
    )
    shed.def_(
        old=r'.. method:: USB_VCP.readinto(buf, [maxlen])',
        new='''
@overload
def readinto(self, buf: _AnyArray, /) -> Optional[int]: ...
@overload
def readinto(self, buf: _AnyArray, maxlen: int, /) -> Optional[int]
''',
        indent=3,
    )
    shed.def_(
        old=r'.. method:: USB_VCP.readline()',
        new='def readline(self) -> Optional[bytes]',
        indent=3,
    )
    shed.def_(
        old=r'.. method:: USB_VCP.readlines()',
        new='def readlines(self) -> Optional[List[bytes]]',
        indent=3,
    )
    shed.def_(
        old=r'.. method:: USB_VCP.write(buf)',
        new='def write(self, buf: Union[_AnyArray, bytes], /) -> int',
        indent=3,
    )
    shed.def_(
        old=r'.. method:: USB_VCP.recv(data, \*, timeout=5000)',
        new='''
@overload
def recv(self, data: int, /, *, timeout: int = 5000) -> Optional[bytes]: ...
@overload
def recv(self, data: _AnyArray, /, *, timeout: int = 5000) -> Optional[int]
''',
        indent=3,
    )
    shed.def_(
        old=r'.. method:: USB_VCP.send(data, \*, timeout=5000)',
        new='def send(self, buf: Union[_AnyArray, bytes, int], /, *, timeout: int = 5000) -> int',
        indent=3,
    )
    shed.constants()


def _uhd(this: str, shed: Typeshed) -> str:
    shed.class_(old=this)
    shed.def_(
        old=r'.. class:: pyb.USB_HID()',
        new='def __init__(self)',
        indent=3,
    )
    shed.def_(
        old=r'.. method:: USB_HID.recv(data, \*, timeout=5000)',
        new='''
@overload
def recv(self, data: int, /, *, timeout: int = 5000) -> bytes: ...
@overload
def recv(self, data: _AnyArray, /, *, timeout: int = 5000) -> int
''',
        indent=3,
    )
    nxt = 'pyb.USB_VCP.rst'
    shed.def_(
        old=r'.. method:: USB_HID.send(data)',
        new='def send(self, data: Sequence[int]) -> None',
        indent=3,
        end=nxt
    )
    return nxt


def _urt(this: str, shed: Typeshed) -> str:
    shed.class_(old=this)
    shed.def_(
        old=r'.. class:: pyb.UART(bus, ...)',
        new='''
@overload
def __init__(
   self, 
   bus: Union[int, str],
   /
): ...
@overload
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
''',
        indent=3
    )
    shed.def_(
        old=(
            r'.. method:: UART.init(baudrate, bits=8, parity=None, stop=1, \*, '
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
        indent=3
    )
    shed.def_(
        old=r'.. method:: UART.deinit()',
        new='def deinit(self) -> None',
        indent=3
    )
    shed.def_(
        old=r'.. method:: UART.any()',
        new='def any(self) -> int',
        indent=3
    )
    shed.def_(
        old=r'.. method:: UART.read([nbytes])',
        new='''
@overload
def read(self) -> Optional[bytes]: ...
@overload
def read(self, nbytes: int, /) -> Optional[bytes]
''',
        indent=3
    )
    shed.def_(
        old=r'.. method:: UART.readchar()',
        new='def readchar(self) -> int',
        indent=3
    )
    shed.def_(
        old=r'.. method:: UART.readinto(buf[, nbytes])',
        new='''
@overload
def readinto(self, buf: _AnyArray, /) -> Optional[int]: ...
@overload
def readinto(self, buf: _AnyArray, nbytes: int, /) -> Optional[int]
''',
        indent=3
    )
    shed.def_(
        old=r'.. method:: UART.readline()',
        new='def readline(self) -> Optional[str]',
        indent=3
    )
    shed.def_(
        old=r'.. method:: UART.write(buf)',
        new='def write(self, buf: _AnyArray, /) -> Optional[int]',
        indent=3
    )
    shed.def_(
        old=r'.. method:: UART.writechar(char)',
        new='def writechar(self, char: int, /) -> None',
        indent=3
    )
    shed.def_(
        old=r'.. method:: UART.sendbreak()',
        new='def sendbreak(self) -> None',
        indent=3
    )
    shed.constants()
    nxt = 'pyb.USB_HID.rst'
    shed.extra_notes(end=nxt)
    return nxt


def _timer_channel(*, old: str, end: str, shed: Typeshed):
    shed.consume_name_line(old)
    shed.consume_title_line()
    shed.consume_blank_line()
    methods = 'Methods'
    doc = []
    for doc_line in shed.lines:
        if doc_line.startswith(methods):
            shed.consume_header_line()
            shed.consume_blank_line()
            break
        doc.append(f'   {doc_line}\n')
    else:
        assert False, f'Did not find: `{methods}`'
    shed.typeshed.append(f'''
class TimerChannel(ABC): 
   """
{''.join(doc).rstrip()}
   """
'''
                         )
    shed.def_(
        old='.. method:: timerchannel.callback(fun)',
        new='''
@abstractmethod
def callback(self, fun: Optional[Callable[[Timer], None]], /) -> None
''',
        indent=3,
    )
    shed.def_(
        old='.. method:: timerchannel.capture([value])',
        new='''
@overload
@abstractmethod
def capture(self) -> int: ...
@overload
@abstractmethod
def capture(self, value: int, /) -> None
''',
        indent=3,
    )
    shed.def_(
        old='.. method:: timerchannel.compare([value])',
        new='''
@overload
@abstractmethod
def compare(self) -> int: ...
@overload
@abstractmethod
def compare(self, value: int, /) -> None
''',
        indent=3,
    )
    shed.def_(
        old='.. method:: timerchannel.pulse_width([value])',
        new='''
@overload
@abstractmethod
def pulse_width(self) -> int: ...
@overload
@abstractmethod
def pulse_width(self, value: int, /) -> None
''',
        indent=3,
    )
    shed.def_(
        old='.. method:: timerchannel.pulse_width_percent([value])',
        new='''
@overload
@abstractmethod
def pulse_width_percent(self) -> float: ...
@overload
@abstractmethod
def pulse_width_percent(self, value: Union[int, float], /) -> None
''',
        indent=3,
        end=end,
    )


def _tim(this: str, shed: Typeshed) -> str:
    shed.class_(
        old=this,
        post_doc='''

   UP: int = ...
   """
   configures the timer to count from 0 to ARR (default).
   """
   
   DOWN: int = ...
   """
   configures the timer to count from ARR down to 0.
   """
   
   CENTER: int = ...
   """
   configures the timer to count from 0 to ARR and then back down to 0.
   """


   PWM: int = ...
   """
   configure the timer in PWM mode (active high).
   """

   PWM_INVERTED: int = ...
   """
   configure the timer in PWM mode (active low).
   """
   
   
   OC_TIMING: int = ...
   """
   indicates that no pin is driven.
   """
   
   OC_ACTIVE: int = ...
   """
   the pin will be made active when a compare match occurs (active is determined by polarity).
   """
   
   OC_INACTIVE: int = ...
   """
   the pin will be made inactive when a compare match occurs.
   """
   
   OC_TOGGLE: int = ...
   """
   the pin will be toggled when an compare match occurs.
   """
   
   OC_FORCED_ACTIVE: int = ...
   """
   the pin is forced active (compare match is ignored).
   """
   
   OC_FORCED_INACTIVE: int = ...
   """
   the pin is forced inactive (compare match is ignored).
   """
   
   
   IC: int = ...
   """
   configure the timer in Input Capture mode.
   """
   
   
   ENC_A: int = ...
   """
   configure the timer in Encoder mode. The counter only changes when CH1 changes.
   """
   
   ENC_B: int = ...
   """
   configure the timer in Encoder mode. The counter only changes when CH2 changes.
   """
   
   ENC_AB: int = ...
   """
   configure the timer in Encoder mode. The counter changes when CH1 or CH2 changes.
   """
   
   
   HIGH: int = ...
   """
   output is active high.
   """
   
   LOW: int = ...
   """
   output is active low.
   """
   
   
   RISING: int = ...
   """
   captures on rising edge.
   """
   
   FALLING: int = ...
   """
   captures on falling edge.
   """
   
   BOTH: int = ...
   """
   captures on both edges.
   """
'''
    )
    shed.def_(
        old=r'.. class:: pyb.Timer(id, ...)',
        new='''
@overload
def __init__(
   self, 
   id: int, 
   /
): ...
@overload
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
): ...
@overload
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
): ...
@overload
def __init__(self, id: int, /): ...
@overload
def __init__(
   self, 
   id: int, 
   /, 
   *, 
   freq: int, 
   mode: int = UP, 
   div: int = 1, 
   callback: Optional[Callable[["Timer"], None]] = None, 
): ...
@overload
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
)
''',
        indent=3
    )
    shed.def_(
        old=r'.. method:: Timer.init(\*, freq, prescaler, period, mode=Timer.UP, div=1, callback=None, deadtime=0)',
        new='''
@overload
def init(
   self, 
   *, 
   freq: int, 
   mode: int = UP, 
   div: int = 1, 
   callback: Optional[Callable[["Timer"], None]] = None, 
   deadtime: int = 0
) -> None: ...
@overload
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
''',
        indent=3
    )
    shed.def_(
        old=r'.. method:: Timer.deinit()',
        new='def deinit(self) -> None',
        indent=3
    )
    shed.def_(
        old=r'.. method:: Timer.callback(fun)',
        new='def callback(self, fun: Optional[Callable[["Timer"], None]], /) -> None',
        indent=3
    )
    shed.def_(
        old=r'.. method:: Timer.channel(channel, mode, ...)',
        new='''
@overload
def channel(
   self, 
   channel: int, 
   /
) -> Optional["TimerChannel"]: ...
@overload
def channel(
   self, 
   channel: int, 
   /, 
   mode: int, 
   *, 
   callback: Optional[Callable[["Timer"], None]] = None, 
   pin: Optional[Pin] = None,
   pulse_width: int,
) -> "TimerChannel": ...
@overload
def channel(
   self, 
   channel: int, 
   /, 
   mode: int, 
   *, 
   callback: Optional[Callable[["Timer"], None]] = None, 
   pin: Optional[Pin] = None,
   pulse_width_percent: Union[int, float],
) -> "TimerChannel": ...
@overload
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
) -> "TimerChannel": ...
@overload
def channel(
   self, 
   channel: int, 
   /, 
   mode: int, 
   *, 
   callback: Optional[Callable[["Timer"], None]] = None, 
   pin: Optional[Pin] = None,
   polarity: int,
) -> "TimerChannel": ...
@overload
def channel(
   self, 
   channel: int, 
   /, 
   mode: int, 
   *, 
   callback: Optional[Callable[["Timer"], None]] = None, 
   pin: Optional[Pin] = None,
) -> "TimerChannel"
''',
        indent=3
    )
    shed.def_(
        old='.. method:: Timer.counter([value])',
        new='''
@overload
def counter(self) -> int: ...
@overload
def counter(self, value: int, /) -> None
''',
        indent=3
    )
    shed.def_(
        old='.. method:: Timer.freq([value])',
        new='''
@overload
def freq(self) -> int: ...
@overload
def freq(self, value: int, /) -> None
''',
        indent=3
    )
    shed.def_(
        old='.. method:: Timer.period([value])',
        new='''
@overload
def period(self) -> int: ...
@overload
def period(self, value: int, /) -> None
''',
        indent=3
    )
    shed.def_(
        old='.. method:: Timer.prescaler([value])',
        new='''
@overload
def prescaler(self) -> int: ...
@overload
def prescaler(self, value: int, /) -> None
''',
        indent=3
    )
    timer_channel = 'class TimerChannel --- setup a channel for a timer'
    shed.def_(
        old=r'.. method:: Timer.source_freq()',
        new='def source_freq(self) -> int',
        indent=3,
        end=timer_channel,
    )
    nxt = 'pyb.UART.rst'
    _timer_channel(old=timer_channel, end=nxt, shed=shed)
    return nxt


def _swt(this: str, shed: Typeshed) -> str:
    shed.class_(old=this)
    shed.def_(
        old=r'.. class:: pyb.Switch()',
        new='def __init__(self)',
        indent=3
    )
    shed.def_(
        old=r'.. method:: Switch.__call__()',
        new='def __call__(self) -> bool',
        indent=3
    )
    shed.def_(
        old=r'.. method:: Switch.value()',
        new='def value(self) -> bool',
        indent=3
    )
    nxt = 'pyb.Timer.rst'
    shed.def_(
        old=r'.. method:: Switch.callback(fun)',
        new='def callback(self, fun: Optional[Callable[[], None]]) -> None',
        indent=3,
        end=nxt
    )
    return nxt


def _spi(this: str, shed: Typeshed) -> str:
    shed.class_(old=this)
    shed.def_(
        old='.. class:: pyb.SPI(bus, ...)',
        new='''
@overload
def __init__(self, bus: int, /): ...
@overload
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
): ...
@overload
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
''',
        indent=3
    )
    shed.def_(
        old=r'.. method:: SPI.deinit()',
        new='def deinit(self) -> None',
        indent=3
    )
    shed.def_(
        old=(
            r'.. method:: SPI.init(mode, baudrate=328125, \*, prescaler, '
            r'polarity=1, phase=0, bits=8, firstbit=SPI.MSB, ti=False, crc=None)'
        ),
        new='''
@overload
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
): ...
@overload
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
''',
        indent=3
    )
    shed.def_(
        old=r'.. method:: SPI.recv(recv, \*, timeout=5000)',
        new='def recv(self, recv: Union[int, _AnyArray], /, *, timeout: int = 5000) -> _AnyArray',
        indent=3
    )
    shed.def_(
        old=r'.. method:: SPI.send(send, \*, timeout=5000)',
        new='def send(self, send: Union[int, _AnyArray, bytes], /, *, timeout: int = 5000) -> None',
        indent=3
    )
    shed.def_(
        old=r'.. method:: SPI.send_recv(send, recv=None, \*, timeout=5000)',
        new='''
def send_recv(
   self, 
   send: Union[int, bytearray, array, bytes], 
   recv: Optional[_AnyArray] = None, 
   /, 
   *, 
   timeout: int = 5000
) -> _AnyArray
''',
        indent=3
    )
    shed.constants()
    return 'pyb.Switch.rst'


def _svo(this: str, shed: Typeshed) -> str:
    shed.class_(old=this)
    shed.def_(
        old='.. class:: pyb.Servo(id)',
        new='def __init__(self, id: int, /)',
        indent=3
    )
    shed.def_(
        old='.. method:: Servo.angle([angle, time=0])',
        new='''
@overload
def angle(self) -> int: ...
@overload
def angle(self, angle: int, time: int = 0, /) -> None
''',
        indent=3
    )
    shed.def_(
        old='.. method:: Servo.speed([speed, time=0])',
        new='''
@overload
def speed(self) -> int: ...
@overload
def speed(self, speed: int, time: int = 0, /) -> None
''',
        indent=3
    )
    shed.def_(
        old='.. method:: Servo.pulse_width([value])',
        new='''
@overload
def speed(self) -> int: ...
@overload
def speed(self, value: int, /) -> None
''',
        indent=3
    )
    nxt = 'pyb.SPI.rst'
    shed.def_(
        old='.. method:: Servo.calibration([pulse_min, pulse_max, pulse_centre, [pulse_angle_90, pulse_speed_100]])',
        new='''
@overload
def calibration(
   self
) -> Tuple[int, int, int, int, int]: ...
@overload
def calibration(
   self, 
   pulse_min: int, 
   pulse_max: int, 
   pulse_centre: int, 
   /
) -> None: ...
@overload
def calibration(
   self, 
   pulse_min: int, 
   pulse_max: int, 
   pulse_centre: int, 
   pulse_angle_90: int, 
   pulse_speed_100: int, 
   /
) -> None
''',
        indent=3,
        end=nxt
    )
    return nxt


def _rtc(this: str, shed: Typeshed) -> str:
    shed.class_(old=this)
    shed.def_(
        old='.. class:: pyb.RTC()',
        new='def __init__(self)',
        indent=3
    )
    shed.def_(
        old='.. method:: RTC.datetime([datetimetuple])',
        new='def datetime(self, datetimetuple: Tuple[int, int, int, int, int, int, int, int], /) -> None',
        indent=3
    )
    shed.def_(
        old='.. method:: RTC.wakeup(timeout, callback=None)',
        new='def wakeup(self, timeout: Optional[Callable[["RTC"], None]] = None, /) -> None',
        indent=3
    )
    shed.def_(
        old='.. method:: RTC.info()',
        new='def info(self) -> int',
        indent=3
    )
    nxt = 'pyb.Servo.rst'
    shed.def_(
        old='.. method:: RTC.calibration(cal)',
        new='''
@overload
def calibration(self) -> int: ...
@overload
def calibration(self, cal: int, /) -> None
''',
        indent=3,
        end=nxt
    )
    return nxt


def _pin_af(*, end: str, shed: Typeshed):
    shed.consume_name_line('class PinAF -- Pin Alternate Functions')
    shed.consume_title_line()
    shed.consume_blank_line()
    doc = []
    for doc_line in shed.lines:
        if doc_line.startswith('Methods'):
            shed.consume_header_line()
            shed.consume_blank_line()
            break
        doc.append(f'   {doc_line}\n')
    else:
        assert False, f'Expected `{end}`, but did not find it!'
    shed.typeshed.append(f'''
class PinAF(ABC): 
   """
{''.join(doc).rstrip()}
   """

   __slots__ = ()
'''
                         )
    shed.def_(
        old='.. method:: pinaf.__str__()',
        new='''
@abstractmethod
def __str__(self) -> str
''',
        indent=3,
    )
    shed.def_(
        old='.. method:: pinaf.index()',
        new='''
@abstractmethod
def index(self) -> int
''',
        indent=3,
    )
    shed.def_(
        old='.. method:: pinaf.name()',
        new='''
@abstractmethod
def name(self) -> str
''',
        indent=3,
    )
    shed.def_(
        old='.. method:: pinaf.reg()',
        new='''
@abstractmethod
def reg(self) -> int
''',
        indent=3,
        end=end
    )


def _pin(this: str, shed: Typeshed) -> str:
    shed.class_(
        old=this,
        post_doc='''
   
   AF1_TIM1: "PinAF" = ...
   """
   Alternate def_ 1, timer 1.
   """
   
   AF1_TIM2: "PinAF" = ...
   """
   Alternate def_ 1, timer 2.
   """

   AF2_TIM3: "PinAF" = ...
   """
   Alternate def_ 2, timer 3.
   """

   AF2_TIM4: "PinAF" = ...
   """
   Alternate def_ 2, timer 4.
   """

   AF2_TIM5: "PinAF" = ...
   """
   Alternate def_ 2, timer 5.
   """

   AF3_TIM10: "PinAF" = ...
   """
   Alternate def_ 3, timer 10.
   """

   AF3_TIM11: "PinAF" = ...
   """
   Alternate def_ 3, timer 11.
   """

   AF3_TIM8: "PinAF" = ...
   """
   Alternate def_ 3, timer 8.
   """

   AF3_TIM9: "PinAF" = ...
   """
   Alternate def_ 3, timer 9.
   """

   AF4_I2C1: "PinAF" = ...
   """
   Alternate def_ 4, I2C 1.
   """

   AF4_I2C2: "PinAF" = ...
   """
   Alternate def_ 4, I2C 2.
   """

   AF5_SPI1: "PinAF" = ...
   """
   Alternate def_ 5, SPI 1.
   """

   AF5_SPI2: "PinAF" = ...
   """
   Alternate def_ 5, SPI 2.
   """

   AF7_USART1: "PinAF" = ...
   """
   Alternate def_ 7, USART 1.
   """

   AF7_USART2: "PinAF" = ...
   """
   Alternate def_ 7, USART 2.
   """

   AF7_USART3: "PinAF" = ...
   """
   Alternate def_ 7, USART 3.
   """

   AF8_UART4: "PinAF" = ...
   """
   Alternate def_ 8, USART 4.
   """

   AF8_USART6: "PinAF" = ...
   """
   Alternate def_ 8, USART 6.
   """

   AF9_CAN1: "PinAF" = ...
   """
   Alternate def_ 9, CAN 1.
   """

   AF9_CAN2: "PinAF" = ...
   """
   Alternate def_ 9, CAN 2.
   """

   AF9_TIM12: "PinAF" = ...
   """
   Alternate def_ 9, timer 12.
   """

   AF9_TIM13: "PinAF" = ...
   """
   Alternate def_ 9, timer 13.
   """

   AF9_TIM14: "PinAF" = ...
   """
   Alternate def_ 9, timer 14.
   """


   ALT: int = ...
   """
   Initialise the pin to alternate-def_ mode with a push-pull drive (same as `AF_PP`).
   """

   ALT_OPEN_DRAIN: int = ...
   """
   Initialise the pin to alternate-def_ mode with an open-drain drive (same as `AF_OD`).
   """

   IRQ_FALLING: int = ...
   """
   Initialise the pin to generate an interrupt on a falling edge.
   """

   IRQ_RISING: int = ...
   """
   Initialise the pin to generate an interrupt on a rising edge.
   """

   OPEN_DRAIN: int = ...
   """
   Initialise the pin to output mode with an open-drain drive (same as `OUT_OD`).
   """
   
   
   class board:
      LED_BLUE: "Pin" = ...
      """
      The blue LED.
      """
      
      LED_GREEN: "Pin" = ...
      """
      The green LED.
      """
      
      LED_RED: "Pin" = ...
      """
      The red LED.
      """
      
      LED_YELLOW: "Pin" = ...
      """
      The yellow LED.
      """
      
      MMA_AVDD: "Pin" = ...
      """
      Accelerometer (MMA7660) analogue power (AVDD) pin.
      """
      
      MMA_INT: "Pin" = ...
      """
      Accelerometer (MMA7660) interrupt (\\INT) pin.
      """
      
      SD: "Pin" = ...
      """
      SD card present switch (0 for card inserted, 1 for no card) (same as SD_SW).
      """

      SD_CK: "Pin" = ...
      """
      SD card clock.
      """

      SD_CMD: "Pin" = ...
      """
      SD card command.
      """

      SD_D0: "Pin" = ...
      """
      SD card serial data 0.
      """

      SD_D1: "Pin" = ...
      """
      SD card serial data 1.
      """

      SD_D2: "Pin" = ...
      """
      SD card serial data 2.
      """

      SD_D3: "Pin" = ...
      """
      SD card serial data 3.
      """

      SD_SW: "Pin" = ...
      """
      SD card present switch (0 for card inserted, 1 for no card) (same as SD).
      """

      SW: "Pin" = ...
      """
      Usr switch (0 = pressed, 1 = not pressed).
      """

      USB_DM: "Pin" = ...
      """
      USB data -.
      """

      USB_DP: "Pin" = ...
      """
      USB data +.
      """

      USB_ID: "Pin" = ...
      """
      USB OTG (on-the-go) ID.
      """

      USB_VBUS: "Pin" = ...
      """
      USB VBUS (power) monitoring pin.
      """

      X1: "Pin" = ...
      """
      X1 pin.
      """

      X10: "Pin" = ...
      """
      X10 pin.
      """

      X11: "Pin" = ...
      """
      X11 pin.
      """

      X12: "Pin" = ...
      """
      X12 pin.
      """

      X17: "Pin" = ...
      """
      X17 pin.
      """

      X18: "Pin" = ...
      """
      X18 pin.
      """

      X19: "Pin" = ...
      """
      X19 pin.
      """

      X2: "Pin" = ...
      """
      X2 pin.
      """

      X20: "Pin" = ...
      """
      X20 pin.
      """

      X21: "Pin" = ...
      """
      X21 pin.
      """
             
      X22: "Pin" = ...
      """
      X22 pin.
      """

      X3: "Pin" = ...
      """
      X3 pin.
      """

      X4: "Pin" = ...
      """
      X4 pin.
      """

      X5: "Pin" = ...
      """
      X5 pin.
      """

      X6: "Pin" = ...
      """
      X6 pin.
      """

      X7: "Pin" = ...
      """
      X7 pin.
      """

      X8: "Pin" = ...
      """
      X8 pin.
      """

      X9: "Pin" = ...
      """
      X9 pin.
      """

      Y1: "Pin" = ...
      """
      Y1 pin.
      """

      Y10: "Pin" = ...
      """
      Y10 pin.
      """

      Y11: "Pin" = ...
      """
      Y11 pin.
      """

      Y12: "Pin" = ...
      """
      Y12 pin.
      """

      Y2: "Pin" = ...
      """
      Y2 pin.
      """

      Y3: "Pin" = ...
      """
      Y3 pin.
      """

      Y4: "Pin" = ...
      """
      Y4 pin.
      """

      Y5: "Pin" = ...
      """
      Y5 pin.
      """

      Y6: "Pin" = ...
      """
      Y6 pin.
      """

      Y7: "Pin" = ...
      """
      Y7 pin.
      """

      Y8: "Pin" = ...
      """
      Y8 pin.
      """

      Y9: "Pin" = ...
      """
      Y9 pin.
      """
   
   
   class cpu:
      A0: "Pin" = ...
      """
      A0 pin.
      """
      
      A1: "Pin" = ...
      """
      A1 pin.
      """

      A10: "Pin" = ...
      """
      A10 pin.
      """

      A11: "Pin" = ...
      """
      A11 pin.
      """

      A12: "Pin" = ...
      """
      A12 pin.
      """

      A13: "Pin" = ...
      """
      A13 pin.
      """

      A14: "Pin" = ...
      """
      A14 pin.
      """

      A15: "Pin" = ...
      """
      A15 pin.
      """

      A2: "Pin" = ...
      """
      A2 pin.
      """

      A3: "Pin" = ...
      """
      A3 pin.
      """

      A4: "Pin" = ...
      """
      A4 pin.
      """

      A5: "Pin" = ...
      """
      A5 pin.
      """

      A6: "Pin" = ...
      """
      A6 pin.
      """

      A7: "Pin" = ...
      """
      A7 pin.
      """

      A8: "Pin" = ...
      """
      A8 pin.
      """

      A9: "Pin" = ...
      """
      A9 pin.
      """

      B0: "Pin" = ...
      """
      B0 pin.
      """

      B1: "Pin" = ...
      """
      B1 pin.
      """

      B10: "Pin" = ...
      """
      B10 pin.
      """

      B11: "Pin" = ...
      """
      B11 pin.
      """

      B12: "Pin" = ...
      """
      B12 pin.
      """

      B13: "Pin" = ...
      """
      B13 pin.
      """

      B14: "Pin" = ...
      """
      B14 pin.
      """

      B15: "Pin" = ...
      """
      B15 pin.
      """

      B2: "Pin" = ...
      """
      B2 pin.
      """

      B3: "Pin" = ...
      """
      B3 pin.
      """

      B4: "Pin" = ...
      """
      B4 pin.
      """

      B5: "Pin" = ...
      """
      B5 pin.
      """

      B6: "Pin" = ...
      """
      B6 pin.
      """

      B7: "Pin" = ...
      """
      B7 pin.
      """

      B8: "Pin" = ...
      """
      B8 pin.
      """

      B9: "Pin" = ...
      """
      B9 pin.
      """

      C0: "Pin" = ...
      """
      C0 pin.
      """

      C1: "Pin" = ...
      """
      C1 pin.
      """

      C10: "Pin" = ...
      """
      C10 pin.
      """

      C11: "Pin" = ...
      """
      C11 pin.
      """

      C12: "Pin" = ...
      """
      C12 pin.
      """

      C13: "Pin" = ...
      """
      C13 pin.
      """

      C2: "Pin" = ...
      """
      C2 pin.
      """

      C3: "Pin" = ...
      """
      C3 pin.
      """

      C4: "Pin" = ...
      """
      C4 pin.
      """

      C5: "Pin" = ...
      """
      C5 pin.
      """

      C6: "Pin" = ...
      """
      C6 pin.
      """

      C7: "Pin" = ...
      """
      C7 pin.
      """

      C8: "Pin" = ...
      """
      C8 pin.
      """

      C9: "Pin" = ...
      """
      C9 pin.
      """

      D2: "Pin" = ...
      """
      D2 pin.
      """
''')
    shed.def_(
        old='.. class:: pyb.Pin(id, ...)',
        new='def __init__(self, id: str, /, mode: int = IN, pull: int = PULL_NONE, af: Union[str, int] = -1)',
        indent=3
    )
    shed.def_(
        old='.. classmethod:: Pin.debug([state])',
        new='''
@staticmethod
@overload
def debug() -> bool: ...
@staticmethod
@overload
def debug(state: bool, /) -> None
''',
        indent=3
    )
    shed.def_(
        old='.. classmethod:: Pin.dict([dict])',
        new='''
@staticmethod
@overload
def dict() -> Dict[str, "Pin"]: ...
@staticmethod
@overload
def dict(dict: Dict[str, "Pin"], /) -> None
''',
        indent=3
    )
    shed.def_(
        old='.. classmethod:: Pin.mapper([fun])',
        new='''
@staticmethod
@overload
def mapper() -> Callable[[str], "Pin"]: ...
@staticmethod
@overload
def mapper(fun: Callable[[str], "Pin"], /) -> None
''',
        indent=3
    )
    shed.def_(
        old='.. method:: Pin.init(mode, pull=Pin.PULL_NONE, af=-1)',
        new='def init(self, mode: int = IN, pull: int = PULL_NONE, af: Union[str, int] = -1) -> None',
        indent=3
    )
    shed.def_(
        old='.. method:: Pin.value([value])',
        new='''
@overload
def value(self) -> int: ...
@overload
def value(self, value: Any, /) -> None
''',
        indent=3
    )
    shed.def_(
        old='.. method:: Pin.__str__()',
        new='def __str__(self) -> str',
        indent=3
    )
    shed.def_(
        old='.. method:: Pin.af()',
        new='def af(self) -> int',
        indent=3
    )
    shed.def_(
        old='.. method:: Pin.af_list()',
        new='def af_list(self) -> List["PinAF"]',
        indent=3
    )
    shed.def_(
        old='.. method:: Pin.gpio()',
        new='def gpio(self) -> int',
        indent=3
    )
    shed.def_(
        old='.. method:: Pin.mode()',
        new='def mode(self) -> int',
        indent=3
    )
    shed.def_(
        old='.. method:: Pin.name()',
        new='def name(self) -> str',
        indent=3
    )
    shed.def_(
        old='.. method:: Pin.names()',
        new='def names(self) -> List[str]',
        indent=3
    )
    shed.def_(
        old='.. method:: Pin.pin()',
        new='def pin(self) -> int',
        indent=3
    )
    shed.def_(
        old='.. method:: Pin.port()',
        new='def port(self) -> int',
        indent=3
    )
    shed.def_(
        old='.. method:: Pin.pull()',
        new='def pull(self) -> int',
        indent=3
    )
    shed.constants()
    nxt = 'pyb.RTC.rst'
    _pin_af(end=nxt, shed=shed)
    return nxt


def _led(this: str, shed: Typeshed) -> str:
    shed.class_(old=this)
    shed.def_(
        old='.. class:: pyb.LED(id)',
        new='def __init__(self, id: int, /)',
        indent=3
    )
    shed.def_(
        old='.. method:: LED.intensity([value])',
        new='''
@overload
def intensity(self) -> int: ...
@overload
def intensity(self, value: int, /) -> None
''',
        indent=3
    )
    shed.def_(
        old='.. method:: LED.off()',
        new='def off(self) -> None',
        indent=3
    )
    shed.def_(
        old='.. method:: LED.on()',
        new='def on(self) -> None',
        indent=3
    )
    nxt = 'pyb.Pin.rst'
    shed.def_(
        old='.. method:: LED.toggle()',
        new='def toggle(self) -> None',
        indent=3,
        end=nxt
    )
    return nxt


def _lcd(this: str, shed: Typeshed) -> str:
    shed.class_(old=this)
    shed.def_(
        old='.. class:: pyb.LCD(skin_position)',
        new='def __init__(self, skin_position: str, /)',
        indent=3
    )
    shed.def_(
        old='.. method:: LCD.command(instr_data, buf)',
        new='def command(self, inst_data: int, buf: bytes, /) -> None',
        indent=3
    )
    shed.def_(
        old='.. method:: LCD.contrast(value)',
        new='def contrast(self, value: int, /) -> None',
        indent=3
    )
    shed.def_(
        old='.. method:: LCD.fill(colour)',
        new='def fill(self, colour: int, /) -> None',
        indent=3
    )
    shed.def_(
        old='.. method:: LCD.get(x, y)',
        new='def get(self, x: int, y: int, /) -> int',
        indent=3
    )
    shed.def_(
        old='.. method:: LCD.light(value)',
        new='def light(self, value: Union[bool, int], /) -> None',
        indent=3
    )
    shed.def_(
        old='.. method:: LCD.pixel(x, y, colour)',
        new='def pixel(self, x: int, y: int, colour: int, /) -> None',
        indent=3
    )
    shed.def_(
        old='.. method:: LCD.show()',
        new='def show(self) -> None',
        indent=3
    )
    shed.def_(
        old='.. method:: LCD.text(str, x, y, colour)',
        new='def text(self, str: str, x: int, y: int, colour: int, /) -> None',
        indent=3
    )
    nxt = 'pyb.LED.rst'
    shed.def_(
        old='.. method:: LCD.write(str)',
        new='def write(self, str: str, /) -> None',
        indent=3,
        end=nxt
    )
    return nxt


def _i2c(this: str, shed: Typeshed) -> str:
    shed.class_(old=this, )
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
   baudrate: int = 400000, 
   gencall: bool = False, 
   dma: bool = False
)
''',
        indent=3
    )
    shed.def_(
        old=r'.. method:: I2C.deinit()',
        new='def deinit(self) -> None',
        indent=3
    )
    shed.def_(
        old=r'.. method:: I2C.init(mode, \*, addr=0x12, baudrate=400000, gencall=False, dma=False)',
        new='''
def init(
   self, 
   bus: Union[int, str], 
   mode: str, 
   /, 
   *, 
   addr: int = 0x12, 
   baudrate: int = 400000, 
   gencall: bool = False, 
   dma: bool = False
) -> None
''',
        indent=3
    )
    shed.def_(
        old=r'.. method:: I2C.is_ready(addr)',
        new='def is_ready(self, addr: int, /) -> bool',
        indent=3
    )
    shed.def_(
        old=r'.. method:: I2C.mem_read(data, addr, memaddr, \*, timeout=5000, addr_size=8)',
        new='''
def mem_read(
   self, 
   data: Union[int, _AnyArray], 
   addr: int, 
   memaddr: int,
   /, 
   *, 
   timeout: int = 5000, 
   addr_size: int = 8, 
) -> bytes
''',
        indent=3
    )
    return 'pyb.LCD.rst'


def _flh(this: str, shed: Typeshed) -> str:
    shed.class_(old=this, )
    shed.def_(
        old='.. class:: pyb.Flash()',
        new='''
@overload
def __init__(self)
''',
        indent=3,
    )
    shed.def_(
        old=r'.. class:: pyb.Flash(\*, start=-1, len=-1)',
        new='''
@overload
def __init__(self, *, start: int = -1, len: int = -1)
''',
        indent=3
    )
    shed.defs(
        class_='Flash',
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
    )
    nxt = 'pyb.I2C.rst'
    shed.extra_notes(end=nxt)
    return nxt


def _eit(this: str, shed: Typeshed):
    shed.class_(old=this, )
    shed.def_(
        old='.. class:: pyb.ExtInt(pin, mode, pull, callback)',
        new='def __init__(self, pin: Union[int, str, "Pin"], mode: int, pull: int, callback: Callable[[int], None])',
        indent=3
    )
    shed.def_(
        old='.. classmethod:: ExtInt.regs()',
        new='''
@staticmethod
def regs() -> None
''',
        indent=3
    )
    shed.def_(
        old='.. method:: ExtInt.disable()',
        new='def disable(self) -> None',
        indent=3
    )
    shed.def_(
        old='.. method:: ExtInt.enable()',
        new='def enable(self) -> None',
        indent=3
    )
    shed.def_(
        old='.. method:: ExtInt.line()',
        new='def line(self) -> int',
        indent=3
    )
    shed.def_(
        old='.. method:: ExtInt.swint()',
        new='def swint(self) -> None',
        indent=3
    )
    shed.constants()
    return 'pyb.Flash.rst'


def _dac(this: str, shed: Typeshed) -> str:
    shed.class_(
        old=this,
        post_doc='''
      
   NORMAL: int = ...
   """
   Normal mode (output buffer once) for `mode` argument of `write_timed`.
   """
   
   CIRCULAR: int = ...
   """
   Circular mode (output buffer continuously) for `mode` argument of `write_timed`.
   """
''',
    )
    shed.def_(
        old=r'.. class:: pyb.DAC(port, bits=8, \*, buffering=None)',
        new='def __init__(self, port: Union[int, "Pin"], /, bits: int = 8, *, buffering: Optional[bool] = None)',
        indent=3,
    )
    shed.def_(
        old=r'.. method:: DAC.init(bits=8, \*, buffering=None)',
        new='def init(self, bits: int = 8, *, buffering: Optional[bool] = None) -> None',
        indent=3,
    )
    shed.def_(
        old='.. method:: DAC.deinit()',
        new='def deinit(self) -> None',
        indent=3,
    )
    shed.def_(
        old='.. method:: DAC.noise(freq)',
        new='def noise(self, freq: int, /) -> None',
        indent=3,
    )
    shed.def_(
        old='.. method:: DAC.triangle(freq)',
        new='def triangle(self, freq: int, /) -> None',
        indent=3,
    )
    shed.def_(
        old='.. method:: DAC.write(value)',
        new='def write(self, value: int, /) -> None',
        indent=3,
    )
    nxt = 'pyb.ExtInt.rst'
    shed.def_(
        old=r'.. method:: DAC.write_timed(data, freq, \*, mode=DAC.NORMAL)',
        new='def write_timed(self, data: _AnyArray, freq: Union[int, "Timer"], /, *, mode: int = NORMAL) -> None',
        indent=3,
        end=nxt,
    )
    return nxt


def _can(this: str, shed: Typeshed) -> str:
    shed.class_(old=this, )
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
        indent=3,
    )
    shed.def_(
        old='.. classmethod:: CAN.initfilterbanks(nr)',
        new='''
@staticmethod
def initfilterbanks(nr: int, /) -> None
''',
        indent=3,
    )
    shed.def_(
        old=r'.. method:: CAN.init(mode, extframe=False, prescaler=100, \*, sjw=1, bs1=6, bs2=8, auto_restart=False)',
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
   auto_restart: bool = False
) -> None
''',
        indent=3,
    )
    shed.def_(
        old='.. method:: CAN.deinit()',
        new='def deinit(self) -> None',
        indent=3,
    )
    shed.def_(
        old='.. method:: CAN.restart()',
        new='def restart(self) -> None',
        indent=3,
    )
    shed.def_(
        old='.. method:: CAN.state()',
        new='def state(self) -> int',
        indent=3,
    )
    shed.def_(
        old='.. method:: CAN.info([list])',
        new='''
@overload
def info(self) -> List[int]: ...
@overload
def info(self, list: List[int], /) -> List[int]
''',
        indent=3,
    )
    shed.def_(
        old=r'.. method:: CAN.setfilter(bank, mode, fifo, params, \*, rtr)',
        new='''
@overload
def setfilter(self, bank: int, mode: int, fifo: int, params: Sequence[int], /) -> None: ...
@overload
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
''',
        indent=3,
    )
    shed.def_(
        old='.. method:: CAN.clearfilter(bank)',
        new='def clearfilter(self, bank: int, /) -> None',
        indent=3,
    )
    shed.def_(
        old='.. method:: CAN.any(fifo)',
        new='def any(self, fifo: int, /) -> bool',
        indent=3,
    )
    shed.def_(
        old=r'.. method:: CAN.recv(fifo, list=None, \*, timeout=5000)',
        new='''
@overload
def recv(self, fifo: int, /, *, timeout: int = 5000) -> Tuple[int, bool, int, memoryview]: ...
@overload
def recv(self, fifo: int, list: None, /, *, timeout: int = 5000) -> Tuple[int, bool, int, memoryview]: ...
@overload
def recv(self, fifo: int, list: List[Union[int, bool, memoryview]], /, *, timeout: int = 5000) -> None
''',
        indent=3,
    )
    shed.def_(
        old=r'.. method:: CAN.send(data, id, \*, timeout=0, rtr=False)',
        new='def send(self, data: Union[int, _AnyArray], id: int, /, *, timeout: int = 0, rtr: bool = False) -> None',
        indent=3,
    )
    shed.def_(
        old='.. method:: CAN.rxcallback(fifo, fun)',
        new='def rxcallback(self, fifo: int, fun: Callable[["CAN"], None], /) -> None',
        indent=3,
    )
    shed.constants()
    return 'pyb.DAC.rst'


def _adc_all(*, this: str, end: str, shed: Typeshed):
    shed.consume_name_line(this)
    shed.consume_header_line()
    shed.consume_blank_line()
    doc = []
    for doc_line in shed.lines:
        if doc_line.lstrip().startswith(end):
            shed.lines.push_line(doc_line)
            break
        doc.append(f'   {doc_line}\n')
    else:
        assert False, f'Did not find: {end}'
    shed.typeshed.append(f'''
class ADCAll: 
   """
{''.join(doc).rstrip()}
   """

   def __init__(self, resolution: int, mask: int = 0xffffffff, /):
      """
      Create a multi-channel ADC instance.

      ``resolution`` is the number of bits for all the ADC's (even those not enabled); one of: 
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
'''
                         )


def _adc(this: str, shed: Typeshed) -> str:
    shed.class_(old=this)
    shed.def_(
        old='.. class:: pyb.ADC(pin)',
        new='def __init__(self, pin: Union[int, "Pin"], /)',
        indent=3
    )
    shed.def_(
        old='.. method:: ADC.read()',
        new='def read(self) -> int',
        indent=3
    )
    shed.def_(
        old='.. method:: ADC.read_timed(buf, timer)',
        new='def read_timed(self, buf: _AnyArray, timer: Union["Timer", int], /) -> None',
        indent=3
    )
    extra = 'The ADCAll Object'
    shed.def_(
        old='.. method:: ADC.read_timed_multi((adcx, adcy, ...), (bufx, bufy, ...), timer)',
        new='''
@staticmethod
def read_timed_multi(
   adcs: Tuple['ADC', ...], 
   bufs: Tuple[_AnyArray, ...], 
   timer: "Timer", 
   /
) -> bool
''',
        indent=3,
        end=extra
    )
    nxt = 'pyb.CAN.rst'
    _adc_all(this=extra, end=nxt, shed=shed)
    return nxt


def _acl(shed: Typeshed) -> str:
    shed.class_(old='pyb.Accel.rst')
    shed.def_(
        old='.. class:: pyb.Accel()',
        new='def __init__(self)',
        indent=3
    )
    shed.def_(
        old='.. method:: Accel.filtered_xyz()',
        new='def filtered_xyz(self) -> Tuple[int, int, int]',
        indent=3
    )
    shed.def_(
        old='.. method:: Accel.tilt()',
        new='def tilt(self) -> int',
        indent=3
    )
    shed.def_(
        old='.. method:: Accel.x()',
        new='def x(self) -> int',
        indent=3
    )
    shed.def_(
        old='.. method:: Accel.y()',
        new='def y(self) -> int',
        indent=3
    )
    shed.def_(
        old='.. method:: Accel.z()',
        new='def z(self) -> int',
        indent=3,
        end='Hardware Note'
    )
    nxt = 'pyb.ADC.rst'
    shed.extra_notes(end=nxt)
    return nxt


def _pyb(*, output_dir: str) -> Typeshed:
    shed = Typeshed(name='pyb', output_dir=output_dir)
    shed.module(
        old='functions related to the board',
        post_doc='''
from abc import ABC, abstractmethod
from typing import NoReturn, overload, Tuple, Sequence, runtime_checkable, Protocol
from typing import Optional, Union, TypeVar, List, Callable, Dict, Any

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


@runtime_checkable
class _AbstractBlockDev(Protocol):
    """
    A `Protocol` (structurally typed) with the defs needed by 
    `usb_mode` argument `msc`.
    """

    __slots__ = ()

    @abstractmethod
    def readblocks(self, blocknum: int, buf: bytes, offset: int = 0, /) -> None: ... 

    @abstractmethod
    def writeblocks(self, blocknum: int, buf: bytes, offset: int = 0, /) -> None: ...

    @abstractmethod
    def ioctl(self, op: int, arg: int) -> Optional[int]: ...


hid_mouse: Tuple[int, int, int, int, bytes] = ...
"""
Mouse human interface device (hid), see `hid` argument of `usb_mode`.
"""


hid_keyboard: Tuple[int, int, int, int, bytes] = ...
"""
Keyboard human interface device (hid), see `hid` argument of `usb_mode`.
"""


_AnyArray = TypeVar('_AnyArray', bytearray, array, memoryview)
"""
Type that allows either bytearray or array but not mixture of both; exclusively one or the other.
"""
''',
    )
    shed.def_(
        old='.. function:: delay(ms)',
        new='def delay(ms: int, /) -> None'
    )
    shed.def_(
        old='.. function:: udelay(us)',
        new='def udelay(us: int, /) -> None'
    )
    shed.def_(
        old='.. function:: millis()',
        new='def millis() -> int'
    )
    shed.def_(
        old='.. function:: micros()',
        new='def micros() -> int'
    )
    shed.def_(
        old='.. function:: elapsed_millis(start)',
        new='def elapsed_millis(start: int, /) -> int'
    )
    shed.def_(
        old='.. function:: elapsed_micros(start)',
        new='def elapsed_micros(start: int, /) -> int'
    )
    shed.def_(
        old='.. function:: hard_reset()',
        new='def hard_reset() -> NoReturn'
    )
    shed.def_(
        old='.. function:: bootloader()',
        new='def bootloader() -> NoReturn'
    )
    shed.def_(
        old='.. function:: fault_debug(value)',
        new='def fault_debug(value: bool = False) -> None'
    )
    shed.def_(
        old='.. function:: disable_irq()',
        new='def disable_irq() -> bool'
    )
    shed.def_(
        old='.. function:: enable_irq(state=True)',
        new='def enable_irq(state: bool = True, /) -> None'
    )
    shed.def_(
        old='.. function:: freq([sysclk[, hclk[, pclk1[, pclk2]]]])',
        new='''
@overload
def freq() -> Tuple[int, int, int, int]: ...
@overload
def freq(sysclk: int, /) -> None: ...
@overload
def freq(sysclk: int, hclk: int, /) -> None: ...
@overload
def freq(sysclk: int, hclk: int, pclk1: int, /) -> None: ...
@overload
def freq(sysclk: int, hclk: int, pclk1: int, pclk2: int, /) -> None
''',
    )
    shed.def_(
        old='.. function:: wfi()',
        new='def wfi() -> None'
    )
    shed.def_(
        old='.. function:: stop()',
        new='def stop() -> None'
    )
    shed.def_(
        old='.. function:: standby()',
        new='def standby() -> None'
    )
    shed.def_(
        old='.. function:: have_cdc()',
        new='def have_cdc() -> bool'
    )
    shed.def_(
        old='.. function:: hid((buttons, x, y, z))',
        new='''
@overload
def hid(data: Tuple[int, int, int, int], /) -> None: ...
@overload
def hid(data: Sequence[int], /) -> None
''',
    )
    shed.def_(
        old='.. function:: info([dump_alloc_table])',
        new='''
@overload
def info() -> None: ...
@overload
def info(dump_alloc_table: bytes, /) -> None
''',
    )
    shed.def_(
        old='.. function:: main(filename)',
        new='def main(filename: str, /) -> None'
    )
    shed.def_(
        old=r'.. function:: mount(device, mountpoint, \*, readonly=False, mkfs=False)',
        new='''
@overload
def mount(
   device: _OldAbstractReadOnlyBlockDev, 
   mountpoint: str, 
   /, 
   *, 
   readonly: bool = False, 
   mkfs: bool = False
) -> None: ...
@overload
def mount(
   device: _OldAbstractBlockDev, 
   mountpoint: str, 
   /, 
   *, 
   readonly: bool = False, 
   mkfs: bool = False
) -> None
''',
    )
    shed.def_(
        old='.. function:: repl_uart(uart)',
        new='''
@overload
def repl_uart() -> Optional['UART']: ...
@overload
def repl_uart(uart: 'UART', /) -> None
''',
    )
    shed.def_(
        old='.. function:: rng()',
        new='def rng() -> int'
    )
    shed.def_(
        old='.. function:: sync()',
        new='def sync() -> None'
    )
    shed.def_(
        old='.. function:: unique_id()',
        new='def unique_id() -> bytes'
    )
    shed.def_(
        old=(
            '.. function:: usb_mode('
            '[modestr], port=-1, vid=0xf055, pid=-1, msc=(), hid=pyb.hid_mouse, high_speed=False)'
        ),
        new='''
@overload
def usb_mode() -> str: ...
@overload
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
''',
        end='Classes',
    )
    return shed
