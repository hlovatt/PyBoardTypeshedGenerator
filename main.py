#!/usr/bin/env python3


from sys import argv

import lines
from lcd160cr import lcd160cr
from pyb import pyb
from typeshed import Typeshed
from uarray import uarray

__author__ = lines.__author__
__copyright_ = lines.__copyright__
__license__ = lines.__license__
__version__ = lines.__version__


def main() -> None:
    assert len(argv) == 2, '''
No destination directory given; usage (from `ByBoardTypeshedGenerator`'s directory) one of:
  1. `python3 main.py <destination directory>`.
  2. `./main.py <destination directory>` (if `main.py` is executable).
'''
    shed = Typeshed(output_dir=argv[1])
    uarray(shed)
    pyb(shed)
    lcd160cr(shed)


if __name__ == '__main__':
    main()
