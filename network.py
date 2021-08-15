"""
Generate `pyi` from corresponding `rst` docs.
"""

import rst
from rst2pyi import RST2PyI

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = "5.0.0"  # Version set by https://github.com/hlovatt/tag2ver


def network(shed: RST2PyI) -> None:
    _network(shed)
    nxt = _wlan(shed)
    nxt = _wlanwipy(nxt, shed)
    nxt = _cc3k(nxt, shed)
    _wiznet5k(nxt, shed)
    _network_func(shed)

    shed.write()


def _network_func(shed: RST2PyI) -> None:
    shed.def_(
        old=R'.. function:: phy_mode([mode])',
        new=[
            'def phy_mode(self) -> int',
            'def phy_mode(self, mode: int, /) -> None'
        ],
        indent=0,
    )


def _wiznet5k(this: str, shed: RST2PyI) -> None:
    shed.class_from_file(old=this)
    shed.def_(
        old=R'.. class:: WIZNET5K(spi, pin_cs, pin_rst)',
        new='def __init__(self, spi: pyb.SPI, pin_cs: pyb.Pin, pin_rst: pyb.Pin, /)',
    )
    shed.def_(
        old=R'.. method:: WIZNET5K.isconnected()',
        new='def isconnected(self) -> bool',
    )
    shed.def_(
        old=R'.. method:: WIZNET5K.ifconfig([(ip, subnet, gateway, dns)])',
        new=[
            'def ifconfig(self) -> Tuple[str, str, str, str]',
            'def ifconfig(self, config: Tuple[str, str, str, str], /)',
        ],
    )
    shed.def_(
        old=R'.. method:: WIZNET5K.regs()',
        new='def regs(self) -> Any',
        end='Network functions',
    )


def _cc3k(this: str, shed: RST2PyI) -> str:
    shed.class_from_file(old=this)
    shed.def_(
        old=R'.. class:: CC3K(spi, pin_cs, pin_en, pin_irq)',
        new='def __init__(self, spi: pyb.SPI, pin_cs: pyb.Pin, pin_en: pyb.Pin, pin_irq: pyb.Pin, /)',
    )
    shed.def_(
        old=R'.. method:: CC3K.connect(ssid, key=None, *, security=WPA2, bssid=None)',
        new='''
def connect(
   self, 
   ssid: str, 
   key: Optional[str] = None, 
   /, 
   *, 
   security: int = WPA2,
   bssid: Optional[bytes] = None,
) -> None
''',
    )
    shed.def_(
        old=R'.. method:: CC3K.disconnect()',
        new='def disconnect(self) -> None',
    )
    shed.def_(
        old=R'.. method:: CC3K.isconnected()',
        new='def isconnected(self) -> bool',
    )
    shed.def_(
        old=R'.. method:: CC3K.ifconfig()',
        new='def ifconfig(self) -> Tuple[str, str, str, str, str, str, str]',
    )
    shed.def_(
        old=R'.. method:: CC3K.patch_version()',
        new='def patch_version(self) -> str',
    )
    shed.def_(
        old=R".. method:: CC3K.patch_program('pgm')",
        new='def patch_program(self, cmd: str, /) -> None',
    )
    end = 'network.WIZNET5K.rst'
    shed.vars(
        old=[
            '.. data:: CC3K.WEP',
            '.. data:: CC3K.WPA',
            '.. data:: CC3K.WPA2',
        ],
        end=end,
    )
    return end


def _wlanwipy(this: str, shed: RST2PyI) -> str:
    shed.class_from_file(old=this)
    shed.def_(
        old=R'.. class:: WLANWiPy(id=0, ...)',
        new=['''
def __init__(self, id: int = 0, /)
''', '''
def __init__(self, id: int, /, *, mode: int, ssid: str, auth: Tuple[str, str], channel: int, antenna: int)
''',
             ],
    )
    shed.def_(
        old=R'.. method:: WLANWiPy.init(mode, *, ssid, auth, channel, antenna)',
        new='def init(self, mode: int, /, *, ssid: str, auth: Tuple[str, str], channel: int, antenna: int) -> bool',
    )
    shed.def_(
        old=R'.. method:: WLANWiPy.connect(ssid, *, auth=None, bssid=None, timeout=None)',
        new='''
def connect(
   self, 
   ssid: str, 
   /, 
   *, 
   auth: Optional[Tuple[str, str]] = None, 
   bssid: Optional[bytes] = None,
   timeout: Optional[int] = None,
) -> None
''',
    )
    shed.def_(
        old=R'.. method:: WLANWiPy.scan()',
        new='def scan(self) -> Tuple[str, bytes, int, Optional[int], int]',
    )
    shed.def_(
        old=R'.. method:: WLANWiPy.disconnect()',
        new='def disconnect(self) -> None',
    )
    shed.def_(
        old=R'.. method:: WLANWiPy.isconnected()',
        new='def isconnected(self) -> bool',
    )
    shed.def_(
        old=R".. method:: WLANWiPy.ifconfig(if_id=0, config=['dhcp' or configtuple])",
        new=[
            'def ifconfig(self, if_id: int = 0, /) -> Tuple[str, str, str, str]',
            'def ifconfig(self, if_id: int = 0, /, *, config: Union[str, Tuple[str, str, str, str]]) -> None',
        ],
    )
    shed.def_(
        old=R'.. method:: WLANWiPy.mode([mode])',
        new=[
            'def mode(self) -> int',
            'def mode(self, mode: int, /) -> None'
        ],
    )
    shed.def_(
        old=R'.. method:: WLANWiPy.ssid([ssid])',
        new=[
            'def ssid(self) -> str',
            'def ssid(self, ssid: str, /) -> None'
        ],
    )
    shed.def_(
        old=R'.. method:: WLANWiPy.auth([auth])',
        new=[
            'def auth(self) -> int',
            'def auth(self, auth: int, /) -> None'
        ],
    )
    shed.def_(
        old=R'.. method:: WLANWiPy.channel([channel])',
        new=[
            'def channel(self) -> int',
            'def channel(self, channel: int, /) -> None'
        ],
    )
    shed.def_(
        old=R'.. method:: WLANWiPy.antenna([antenna])',
        new=[
            'def antenna(self) -> int',
            'def antenna(self, antenna: int, /) -> None'
        ],
    )
    shed.def_(
        old=R'.. method:: WLANWiPy.mac([mac_addr])',
        new=[
            'def mac(self) -> bytes',
            'def mac(self, mac: bytes, /) -> None'
        ],
    )
    shed.def_(
        old=R'.. method:: WLANWiPy.irq(*, handler, wake)',
        new='def irq(self, *, handler: Callable[[], None], wake: int) -> Any',
    )
    shed.vars(
        old=[
            '.. data:: WLANWiPy.STA',
            '.. data:: WLANWiPy.AP',
        ],
    )
    shed.vars(
        old=[
            '.. data:: WLANWiPy.WEP',
            '.. data:: WLANWiPy.WPA',
            '.. data:: WLANWiPy.WPA2',
        ],
    )
    end = 'network.CC3K.rst'
    shed.vars(
        old=[
            '.. data:: WLANWiPy.INT_ANT',
            '.. data:: WLANWiPy.EXT_ANT',
        ],
        end=end,
    )
    return end


def _wlan(shed: RST2PyI) -> str:
    shed.class_from_file(old='network.WLAN.rst')
    shed.def_(
        old=R'.. class:: WLAN(interface_id)',
        new='def __init__(self, interface_id: int, /)',
        extra_doc_indent=3,
    )
    shed.def_(
        old=R'.. method:: WLAN.active([is_active])',
        new=[
            'def active(self, /) -> bool',
            'def active(self, is_active: bool, /) -> None',
        ],
    )
    shed.def_(
        old=R'.. method:: WLAN.connect(ssid=None, password=None, *, bssid=None)',
        new='''
def connect(
   self, 
   ssid: Optional[str] = None, 
   password: Optional[str] = None, 
   /, 
   *, 
   bssid: Optional[bytes] = None
) -> None
''',
    )
    shed.def_(
        old=R'.. method:: WLAN.disconnect()',
        new='def disconnect(self) -> None',
    )
    shed.def_(
        old=R'.. method:: WLAN.scan()',
        new='def scan(self) -> Tuple[str, bytes, int, int, int]',
    )
    shed.def_(
        old=R'.. method:: WLAN.status([param])',
        new=[
            'def status(self) -> int',
            'def status(self, param: str, /) -> int'
        ],
    )
    shed.def_(
        old=R'.. method:: WLAN.isconnected()',
        new='def isconnected(self) -> bool',
    )
    shed.def_(
        old=R'.. method:: WLAN.ifconfig([(ip, subnet, gateway, dns)])',
        new=[
            'def ifconfig(self) -> Tuple[str, str, str, str]',
            'def ifconfig(self, ip_mask_gateway_dns: Tuple[str, str, str, str], /) -> None',
        ],
    )
    end = 'network.WLANWiPy.rst'
    shed.defs_with_common_description(
        cmd='.. method:: WLAN.',
        old2new={
            "config('param')":
                '''
@overload
def config(self, param: str, /) -> Any
''',
            'config(param=value, ...)':
                '''
@overload
def config(self, **kwargs: Any) -> None
'''
        },
        end=end,
    )
    return end


def _network(shed: RST2PyI) -> None:
    shed.module(
        name='network',
        old='network configuration',
        post_doc='''
from abc import abstractmethod
from typing import Protocol, List, Tuple, Callable, overload, Any, Optional, ClassVar, Union

import pyb


MODE_11B: int = ...
"""IEEE 802.11b"""

MODE_11G: int = ...
"""IEEE 802.11g"""

MODE_11N: int = ...
"""IEEE 802.11n"""
''',
        end=R'Common network adapter interface',
    )
    constructor = R'.. class:: AbstractNIC(id=None, ...)'
    shed.class_(name='AbstractNIC(Protocol)', end=constructor)
    shed.def_(
        old=constructor,
        new='''
@abstractmethod
def __init__(self, id: Any = None, /, *args: Any, **kwargs: Any)
''',
        extra_doc_indent=3
    )
    shed.def_(
        old=R'.. method:: AbstractNIC.active([is_active])',
        new=['''
@abstractmethod
def active(self, /) -> bool
''', '''
@abstractmethod
def active(self, is_active: bool, /) -> None
''',
             ],
    )
    shed.def_(
        old=R'.. method:: AbstractNIC.connect([service_id, key=None, *, ...])',
        new=['''
@abstractmethod
def connect(self, key: Optional[str] = None, /, **kwargs: Any) -> None
''', '''
@abstractmethod
def connect(self, service_id: Any, key: Optional[str] = None, /, **kwargs: Any) -> None
''',
             ]
    )
    shed.def_(
        old=R'.. method:: AbstractNIC.disconnect()',
        new='''
@abstractmethod
def disconnect(self) -> None
'''
    )
    shed.def_(
        old=R'.. method:: AbstractNIC.isconnected()',
        new='''
@abstractmethod
def isconnected(self) -> bool
'''
    )
    shed.def_(
        old=R'.. method:: AbstractNIC.scan(*, ...)',
        new='''
@abstractmethod
def scan(self, **kwargs: Any) -> List[Tuple[str, ...]]
'''
    )
    shed.def_(
        old=R'.. method:: AbstractNIC.status([param])',
        new=['''
@abstractmethod
def status(self) -> Any
''', '''
@abstractmethod
def status(self, param: str, /) -> Any
'''
             ]
    )
    shed.def_(
        old=R'.. method:: AbstractNIC.ifconfig([(ip, subnet, gateway, dns)])',
        new=['''
@abstractmethod
def ifconfig(self) -> Tuple[str, str, str, str]
''', '''
@abstractmethod
def ifconfig(self, ip_mask_gateway_dns: Tuple[str, str, str, str], /) -> None
''',
             ]
    )
    shed.defs_with_common_description(
        cmd='.. method:: AbstractNIC.',
        old2new={
            "config('param')":
                '''
@overload
@abstractmethod
def config(self, param: str, /) -> Any
''',
            'config(param=value, ...)':
                '''
@overload
@abstractmethod
def config(self, **kwargs: Any) -> None
'''
        },
        end='Specific network class implementations'
    )
