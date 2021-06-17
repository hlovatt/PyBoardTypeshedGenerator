#!/usr/bin/env python3

"""
Convert MicroPython `.rst` documentation files into `.pyi` typeshed stub interfaces.
"""

from sys import argv

import rst
from btree import btree
from cmath_ import cmath
from framebuf import framebuf
from gc_ import gc
from lcd160cr import lcd160cr
from machine import machine
from math_ import math
from micropython import micropython
from network import network
from pyb import pyb
from rst2pyi import RST2PyI
from uarray import uarray
from ubluetooth import ubluetooth
from ucryptolib import ucryptolib
from uctypes import uctypes

__author__ = rst.__author__

from uasyncio import uasyncio

__copyright_ = rst.__copyright__
__license__ = rst.__license__
__version__ = "4.0.0"  # Version set by https://github.com/hlovatt/tag2ver


def main() -> None:
    usage = '''

Usage (from `PyBoardTypeshedGenerator`'s directory) one of:
  1. `python3 main.py <destination directory>`.
  2. `./main.py <destination directory>` (if `main.py` is executable).
'''
    assert len(argv) > 1, 'No destination directory given.' + usage
    assert len(argv) == 2, 'Extra argument(s) given.' + usage
    shed = RST2PyI(output_dir=argv[1])
    uasyncio(shed)
    math(shed)
    gc(shed)
    cmath(shed)
    uctypes(shed)
    ucryptolib(shed)
    ubluetooth(shed)
    network(shed)
    micropython(shed)
    framebuf(shed)
    btree(shed)
    machine(shed)
    lcd160cr(shed)
    uarray(shed)
    pyb(shed)


if __name__ == '__main__':
    main()
