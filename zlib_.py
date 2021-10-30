"""
Generate `pyi` from corresponding `rst` docs.
"""

import rst
from rst2pyi import RST2PyI

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = "7.2.1"  # Version set by https://github.com/hlovatt/tag2ver


def zlib(shed: RST2PyI) -> None:
    shed.module(
        name="zlib",
        old="zlib decompression",
        post_doc="""
from uio import IOBase
""",
        end="Functions",
    )

    shed.def_(
        old=r".. function:: decompress(data, wbits=0, bufsize=0, /)",
        new="def decompress(data: bytes, wbits: int = 0, bufsize: int = 0, /) -> bytes",
        indent=0,
    )
    shed.class_(
        name="DecompIO(IOBase[bytes])",
        extra_docs=[
            "   Steam wrapper that decompresses a given stream containing zlib compressed data."
        ],
        end=".. class",
    )
    shed.def_(
        old=r".. class:: DecompIO(stream, wbits=0, /)",
        new="def __init__(self, stream: IOBase[bytes], wbits: int = 0, /)",
    )

    shed.write(u_also=True)
