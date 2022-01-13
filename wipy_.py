"""
Generate `pyi` from corresponding `rst` docs.
"""

import rst
from rst2pyi import RST2PyI

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = "7.5.2"  # Version set by https://github.com/hlovatt/tag2ver


def wipy(shed: RST2PyI) -> None:
    shed.module(
        name="wipy",
        old="WiPy specific features",
        post_doc="from typing import overload",
        end="Functions",
    )
    shed.def_(
        old=r".. function:: heartbeat([enable])",
        new=["def heartbeat(enable: bool, /) -> None", "def heartbeat() -> bool",],
        indent=0,
    )
    shed.write()
