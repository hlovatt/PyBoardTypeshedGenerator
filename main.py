#!/usr/bin/env python3

"""
Convert MicroPython `.rst` documentation files into `.pyi` typeshed stub interfaces.
"""

from sys import argv

import rst
from array_ import array
from binascii_ import binascii
from bluetooth_ import bluetooth
from btree_ import btree
from cmath_ import cmath
from collections_ import collections
from cryptolib_ import cryptolib
from errno_ import errno
from framebuf_ import framebuf
from gc_ import gc
from hashlib_ import hashlib
from heapq_ import heapq
from io_ import io
from json_ import json
from lcd160cr_ import lcd160cr
from machine_ import machine
from math_ import math
from micropython_ import micropython
from network_ import network
from os_ import os
from pyb_ import pyb
from re_ import re
from rst2pyi import RST2PyI
from select_ import select
from socket_ import socket
from ssl_ import ssl
from struct_ import struct
from sys_ import sys
from thread_ import thread
from time_ import time
from uasyncio_ import uasyncio
from uctypes_ import uctypes

__author__ = rst.__author__

from zlib_ import zlib

__copyright_ = rst.__copyright__
__license__ = rst.__license__
__version__ = "7.0.0"  # Version set by https://github.com/hlovatt/tag2ver


def main() -> None:
    usage = """

Usage (from `PyBoardTypeshedGenerator`'s directory) one of:
  0. `python3 -m main <destination root directory>`.
  1. `python3 main.py <destination root directory>`.
  2. `./main.py <destination root directory>` (if `main.py` is executable).
"""
    assert len(argv) > 1, "No destination root directory given." + usage
    assert len(argv) == 2, "Extra argument(s) given." + usage
    shed = RST2PyI(output_root_dir=argv[1])
    thread(shed)
    zlib(shed)
    time(shed)
    sys(shed)
    struct(shed)
    ssl(shed)
    socket(shed)
    select(shed)
    re(shed)
    os(shed)
    json(shed)
    io(shed)
    heapq(shed)
    hashlib(shed)
    errno(shed)
    collections(shed)
    binascii(shed)
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


if __name__ == "__main__":
    main()
