"""
Generate `pyi` from corresponding `rst` docs.
"""
import repdefs
import rst
from rst2pyi import RST2PyI

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = "6.2.0"  # Version set by https://github.com/hlovatt/tag2ver


def json(shed: RST2PyI) -> None:
    shed.module(
        name='json',
        old='JSON encoding and decoding',
        post_doc=f'''
from types import TracebackType
from typing import Any, Tuple, AnyStr, Final, TypeVar, runtime_checkable, Protocol
from typing import Optional, Type, List

from uarray import array

{repdefs.ANY_READABLE_BUF}
{repdefs.ANY_WRITABLE_BUF}
{repdefs.IO_BASE}
''',
        end='Functions',
    )
    shed.def_(
        old=R'.. function:: dump(obj, stream, separators=None)',
        new='def dump(obj: Any, stream: IOBase[str, Any], separators: Tuple[str, str] | None = None, /) -> None',
        indent=0,
    )
    shed.def_(
        old=R'.. function:: dumps(obj, separators=None)',
        new='def dumps(obj: Any, separators: Tuple[str, str] | None = None) -> str',
        indent=0,
    )
    shed.def_(
        old=R'.. function:: load(stream)',
        new='def load(stream: IOBase[str, Any]) -> Any',
        indent=0,
    )
    shed.def_(
        old=R'.. function:: loads(str)',
        new='def loads(str: AnyStr) -> Any',
        indent=0,
    )
    shed.write(u_also=True)
