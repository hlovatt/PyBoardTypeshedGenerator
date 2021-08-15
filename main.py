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
from array import array
from bluetooth import bluetooth
from cryptolib import cryptolib
from uctypes import uctypes
from uasyncio import uasyncio

__author__ = rst.__author__
__copyright_ = rst.__copyright__
__license__ = rst.__license__
__version__ = "5.0.3"  # Version set by https://github.com/hlovatt/tag2ver


# TODO Add subdirectory destinations micropython, pyboard, and stdlib

def main() -> None:
    usage = '''

Usage (from `PyBoardTypeshedGenerator`'s directory) one of:
  1. `python3 main.py <destination root directory>`.
  2. `./main.py <destination root directory>` (if `main.py` is executable).
'''
    assert len(argv) > 1, 'No destination root directory given.' + usage
    assert len(argv) == 2, 'Extra argument(s) given.' + usage
    shed = RST2PyI(output_root_dir=argv[1])
    uasyncio(shed)
    math(shed)
    gc(shed)
    cmath(shed)
    uctypes(shed)
    cryptolib(shed)
    bluetooth(shed)
    network(shed)
    micropython(shed)
    framebuf(shed)
    btree(shed)
    machine(shed)
    lcd160cr(shed)
    array(shed)
    pyb(shed)


if __name__ == '__main__':
    main()
