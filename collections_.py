"""
Generate `pyi` from corresponding `rst` docs.
"""

import rst
from rst2pyi import RST2PyI

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = "7.5.3"  # Version set by https://github.com/hlovatt/tag2ver


def collections(shed: RST2PyI) -> None:
    shed.module(
        name="collections",
        old="collection and container types",
        post_doc=f"""
from typing import overload, Any, Type, Iterable, TypeVar, Generic, Mapping, Dict, Final

_KT: Final = TypeVar("_KT")
_VT: Final = TypeVar("_VT")
""",
        end=r"Classes",
    )

    shed.class_(
        pre_str="# noinspection PyPep8Naming",
        name=r"deque",
        extra_docs=["Minimal implementation of a deque that implements a FIFO buffer."],
        end=r"Classes",
    )
    shed.def_(
        old=r".. function:: deque(iterable, maxlen[, flags])",
        new="def __init__(self, iterable: tuple[Any], maxlen: int, flags: int = 0, /)",
        end=r"As well as supporting `bool` and `len`, deque objects have the following",
    )
    shed.pyi.classes[-1].defs.append(
        '''
   def __bool__(self) -> bool:
      """
      Returns true if the `deque` isn't empty.
      
      **Note:** The method isn't listed by ``dir(deque)`` and can't be called directly, 
      however ``bool(deque)`` and automatic conversion work!
      """
   
   def __len__(self) -> int:
      """
      Returns the number of items in the `deque`.
      
      **Note:** The method isn't listed by ``dir(deque)`` and can't be called directly, 
      however ``len(deque)`` works!
      """
'''
    )
    shed.consume_containing_line(
        string=r"methods:", and_preceding_lines=True,
    )
    shed.def_(
        old=r".. method:: deque.append(x)", new="def append(self, x: Any, /) -> None",
    )
    shed.def_(
        old=r".. method:: deque.popleft()", new="def popleft(self) -> Any",
    )

    shed.def_(
        old=r".. function:: namedtuple(name, fields)",
        new="def namedtuple(name: str, fields: str | Iterable[str]) -> Type[tuple[Any, ...]]",
        indent=0,
    )

    shed.class_(
        name=r"OrderedDict(Dict[_KT, _VT], Generic[_KT, _VT])",
        extra_docs="When ordered dict is iterated over, keys/items are returned in the order they were added.",
        end=r"..",
    )
    shed.def_(
        old=r".. function:: OrderedDict(...)",
        new=[
            "def __init__(self)",
            "def __init__(self, **kwargs: _VT)",
            "def __init__(self, map: Mapping[_KT, _VT], **kwargs: _VT)",
        ],
    )

    shed.write(u_also=True)
