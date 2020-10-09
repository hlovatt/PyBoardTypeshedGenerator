#!/usr/bin/env python3


from sys import argv

import rst
from btree import btree
from lcd160cr import lcd160cr
from machine import machine
from pyb import pyb
from rst2pyi import RST2PyI
from uarray import uarray

__author__ = rst.__author__
__copyright_ = rst.__copyright__
__license__ = rst.__license__
__version__ = "3.0.0"  # Version set by https://github.com/hlovatt/tag2ver


def main() -> None:
    usage = '''

Usage (from `ByBoardTypeshedGenerator`'s directory) one of:
  1. `python3 main.py <destination directory>`.
  2. `./main.py <destination directory>` (if `main.py` is executable).
'''
    assert len(argv) > 1, 'No destination directory given.' + usage
    assert len(argv) == 2, 'Extra argument(s) given.' + usage
    shed = RST2PyI(output_dir=argv[1])
    btree(shed)
    machine(shed)
    lcd160cr(shed)
    uarray(shed)
    pyb(shed)


if __name__ == '__main__':
    main()
