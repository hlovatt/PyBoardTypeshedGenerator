"""
Generate `pyi` from corresponding `rst` docs.
"""

import rst
from rst2pyi import RST2PyI

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = "7.2.0"  # Version set by https://github.com/hlovatt/tag2ver


def hashlib(shed: RST2PyI) -> None:
    shed.module(
        name="hashlib",
        old="hashing algorithms",
        post_doc=f"""
from abc import ABC
from typing import overload

from uio import AnyReadableBuf
""",
        end="Constructors",
    )
    shed.consume_minuses_underline_line(and_preceding_lines=True)

    shed.class_(
        pre_str="# noinspection PyPep8Naming",
        name='sha256("_Hash")',
        extra_docs=[
            """
   The current generation, modern hashing algorithm (of SHA2 series).
   It is suitable for cryptographically-secure purposes. Included in the
   MicroPython core and any board is recommended to provide this, unless
   it has particular code size constraints.
"""
        ],
        end="..",
    )
    shed.def_(
        old=".. class:: hashlib.sha256([data])",
        new=["def __init__(self)", "def __init__(self, data: AnyReadableBuf)"],
    )

    shed.class_(
        pre_str="# noinspection PyPep8Naming",
        name='sha1("_Hash")',
        extra_docs=[
            """
   A previous generation algorithm. Not recommended for new usages,
   but SHA1 is a part of number of Internet standards and existing
   applications, so boards targeting network connectivity and
   interoperability will try to provide this.
"""
        ],
        end="..",
    )
    shed.def_(
        old=".. class:: hashlib.sha1([data])",
        new=["def __init__(self)", "def __init__(self, data: AnyReadableBuf)"],
    )

    shed.class_(
        pre_str="# noinspection PyPep8Naming",
        name='md5("_Hash")',
        extra_docs=[
            """
   A legacy algorithm, not considered cryptographically secure. Only
   selected boards, targeting interoperability with legacy applications,
   will offer this.
"""
        ],
        end="..",
    )
    shed.def_(
        old=".. class:: hashlib.md5([data])",
        new="def __init__(self, data: AnyReadableBuf = ..., /)",
    )

    shed.class_(
        name="_Hash(ABC)",
        extra_docs=[
            """
   Abstract base class for hashing algorithms that defines methods available in all algorithms.
"""
        ],
        end="..",
    )
    shed.def_(
        old=".. method:: hash.update(data)",
        new="def update(self, data: AnyReadableBuf, /) -> None",
    )
    shed.def_(
        old=".. method:: hash.digest()", new="def digest(self) -> bytes",
    )
    shed.def_(
        old=".. method:: hash.hexdigest()", new="def hexdigest(self) -> str",
    )

    shed.write(u_also=True)
