#!/usr/bin/env python3


from sys import argv

import rst
from lcd160cr import lcd160cr
from machine import machine
from pyb import pyb
from rst2pyi import RST2PyI
from uarray import uarray

__author__ = rst.__author__
__copyright_ = rst.__copyright__
__license__ = rst.__license__
__version__ = rst.__version__


def main() -> None:
    assert len(argv) == 2, '''
No destination directory given; usage (from `ByBoardTypeshedGenerator`'s directory) one of:
  1. `python3 main.py <destination directory>`.
  2. `./main.py <destination directory>` (if `main.py` is executable).
'''
    shed = RST2PyI(output_dir=argv[1])
    uarray(shed)
    machine(shed)
    pyb(shed)
    lcd160cr(shed)


if __name__ == '__main__':
    main()
