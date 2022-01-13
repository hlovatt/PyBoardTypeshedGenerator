"""
Generate `pyi` from corresponding `rst` docs.
"""
from typing import Final

import rst
from rst2pyi import RST2PyI

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = "7.5.0"  # Version set by https://github.com/hlovatt/tag2ver


def timer_wipy(shed: RST2PyI) -> None:
    constructors: Final = "Constructors"
    shed.module(
        name="machine.TimerWiPy",
        old="class TimerWiPy -- control hardware timers",
        post_doc="from typing import overload, ClassVar, Callable",
        end=constructors,
    )

    shed.class_(
        name="Timer",
        post_doc='''
   ONE_SHOT: ClassVar[int] = ...
   """
   One-shot timer mode.
   """

   PERIODIC: ClassVar[int] = ...
   """
   Periodic timer mode.
   """
   
   PWM: ClassVar[int] = ...
   """
   PWM timer mode.
   """

   A: ClassVar[int] = ...
   """
   Selects timer channel A. 
   Must be ORed with B (``Timer.A | Timer.B``) when using a 32-bit timer.
   """
   
   B: ClassVar[int] = ...
   """
   Selects timer channel B. 
   Must be ORed with A (``Timer.A | Timer.B``) when using a 32-bit timer.
   """

   POSITIVE: ClassVar[int] = ...
   """
   Timer channel positive polarity selection (only relevant in PWM mode).
   """
   
   NEGATIVE: ClassVar[int] = ...
   """
   Timer channel negative polarity selection (only relevant in PWM mode).
   """

   TIMEOUT: ClassVar[int] = ...
   """
   Timer channel IRQ triggers on timeout (only relevant in PERIODIC or ONE_SHOT modes).
   """

   MATCH: ClassVar[int] = ...
   """
   Timer channel IRQ triggers on match (only relevant in PWM mode).
   """
''',
        end=constructors,
    )
    shed.def_(
        old=r".. class:: TimerWiPy(id, ...)",
        new="def __init__(self, id: int, mode: int, /, *, width: int = 16)",
        end="Methods",
    )
    shed.def_(
        old=r".. method:: TimerWiPy.init(mode, *, width=16)",
        new="def init(self, mode: int, /, *, width: int = 16) -> None",
    )
    shed.def_(
        old=r".. method:: TimerWiPy.deinit()", new="def deinit(self) -> None",
    )
    shed.def_(
        old=r".. method:: TimerWiPy.channel(channel, **, freq, period, polarity=TimerWiPy.POSITIVE, duty_cycle=0)",
        new=[
            "def channel(self, channel: int, /) -> TimerChannel | None",
            """
def channel(
   self, 
   channel: int, 
   /, 
   *, 
   freq: int, 
   polarity: int = POSITIVE, 
   duty_cycle: int = 0,
) -> TimerChannel
""",
            """
def channel(
   self, 
   channel: int, 
   /, 
   *, 
   period: int, 
   polarity: int = POSITIVE, 
   duty_cycle: int = 0,
) -> TimerChannel
""",
        ],
        end="class TimerChannel",
    )

    shed.class_(name="TimerChannel", end="Methods")
    shed.def_(
        old=r".. method:: timerchannel.irq(*, trigger, priority=1, handler=None)",
        new="""
def irq(
   self, 
   *, 
   trigger: int, 
   priority: int = 1, 
   handler: Callable[[Timer], None] | None = None
) -> Callable[[Timer], None] | None
""",
    )
    shed.def_(
        old=r".. method:: timerchannel.freq([value])",
        new=["def freq(self) -> int", "def freq(self, value: int, /) -> None",],
    )
    shed.def_(
        old=r".. method:: timerchannel.period([value])",
        new=["def period(self) -> int", "def period(self, value: int, /) -> None",],
    )
    shed.def_(
        old=r".. method:: timerchannel.duty_cycle([value])",
        new=[
            "def duty_cycle(self) -> int",
            "def duty_cycle(self, value: int, /) -> None",
        ],
        end="Constants",
    )

    shed.consume_containing_line(
        ".. data:: TimerWiPy.ONE_SHOT", and_preceding_lines=True
    )
    shed.consume_containing_line(".. data:: TimerWiPy.PERIODIC")
    shed.consume_containing_line("Timer operating mode.", and_preceding_lines=True)

    shed.write()
