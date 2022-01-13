"""
Generate `pyi` from corresponding `rst` docs.
"""
import rst
from rst2pyi import RST2PyI

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = "7.5.0"  # Version set by https://github.com/hlovatt/tag2ver


def json(shed: RST2PyI) -> None:
    shed.module(
        name="json",
        old="JSON encoding and decoding",
        post_doc=f"""
from typing import Any, AnyStr

from uio import IOBase
""",
        end="Functions",
    )
    shed.def_(
        old=r".. function:: dump(obj, stream, separators=None)",
        new="def dump(obj: Any, stream: IOBase[str, Any], separators: tuple[str, str] | None = None, /) -> None",
        indent=0,
    )
    shed.def_(
        old=r".. function:: dumps(obj, separators=None)",
        new="def dumps(obj: Any, separators: tuple[str, str] | None = None) -> str",
        indent=0,
    )
    shed.def_(
        old=r".. function:: load(stream)",
        new="def load(stream: IOBase[str, Any]) -> Any",
        indent=0,
    )
    shed.def_(
        old=r".. function:: loads(str)", new="def loads(str: AnyStr) -> Any", indent=0,
    )
    shed.write(u_also=True)
