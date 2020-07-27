#!/usr/bin/env python3


from sys import argv

from pyb import pyb
from uarray import uarray

__author__ = "Howard C Lovatt"
__copyright_ = "Howard C Lovatt, 2020 onwards."
__license__ = "MIT https://opensource.org/licenses/MIT (as used by MicroPython)."
__version__ = "1.0.0"


def main() -> None:
    assert len(argv) == 2, \
'''No destination directory given; usage (from `ByBoardTypeshedGenerator`'s directory) one of:
  1. `python3 main <destination directory>`.
  2. `./main.py <destination directory>` (if `main.py` is executable).'''
    destination = argv[1]
    pyb(output_dir=destination)
    uarray(output_dir=destination)


if __name__ == '__main__':
    main()
