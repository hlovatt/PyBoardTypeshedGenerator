"""
Generate `pyi` from corresponding `rst` docs.
"""
from typing import Final

import rst
from rst2pyi import RST2PyI

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = "7.5.3"  # Version set by https://github.com/hlovatt/tag2ver


def thread(shed: RST2PyI) -> None:
    dummy: Final = "DUMMY END LINE!"
    shed.rst.push_line(dummy)
    shed.module(
        name="_thread", old="multithreading support", end=dummy,
    )
    shed.consume_containing_line(dummy)

    shed.write()
