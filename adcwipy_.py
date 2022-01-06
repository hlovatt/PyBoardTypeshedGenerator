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


def adcwipy(shed: RST2PyI) -> None:
    constructors: Final = "Constructors"
    shed.module(
        name="machine.ADCWiPy",
        old="class ADCWiPy – analog to digital conversion",
        end=constructors,
    )

    shed.class_(name='ADCWiPy', end=constructors)
    shed.def_(
        old=r".. class:: ADCWiPy(id=0, *, bits=12)",
        new="def __init__(self, id: int = 0, *, bits: int = 12)",
        end='Methods',
    )
    shed.def_(
        old=r'.. method:: ADCWiPy.channel(id, *, pin)',
        new=[
            'def channel(self, id: int) -> ADCChannel',
            'def channel(self, *, pin: str) -> ADCChannel',
            'def channel(self, id: int, *, pin: str) -> ADCChannel',
        ],
    )
    shed.def_(old=r'.. method:: ADCWiPy.init()', new='def init(self) -> None')
    shed.def_(old=r'.. method:: ADCWiPy.deinit()', new='def deinit(self) -> None', end='class ADCChannel')

    shed.class_(name='ADCChannel', end='..')
    shed.def_(old=r'.. method:: adcchannel()', new='def __call__(self) -> int')
    shed.def_(old=r'.. method:: adcchannel.value()', new='def value(self) -> int')
    shed.def_(old=r'.. method:: adcchannel.init()', new='def init(self) -> None')
    shed.def_(old=r'.. method:: adcchannel.deinit()', new='def deinit(self) -> None')

    shed.write()
