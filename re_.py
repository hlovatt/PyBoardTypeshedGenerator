"""
Generate `pyi` from corresponding `rst` docs.
"""
from typing import Final

import rst
from rst2pyi import RST2PyI

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = "7.0.0"  # Version set by https://github.com/hlovatt/tag2ver


def re(shed: RST2PyI) -> None:
    shed.module(
        name="re",
        old="regular expressions",
        post_doc=f"""
from typing import AnyStr, Callable, Generic, Final, Any

_StrLike: Final = str | bytes
""",
        end="Functions",
    )

    shed.def_(
        old=r".. function:: compile(regex_str, [flags])",
        new='def compile(regex_str: _StrLike, flags: int = ..., /) -> "ure"',
        indent=0,
    )
    shed.def_(
        old=r".. function:: match(regex_str, string)",
        new='def match(regex_str: _StrLike, string: AnyStr, /) -> "Match[AnyStr]"',
        indent=0,
    )
    shed.def_(
        old=r".. function:: search(regex_str, string)",
        new='def search(regex_str: _StrLike, string: AnyStr, /) -> "Match[AnyStr]"',
        indent=0,
    )
    shed.def_(
        old=r".. function:: sub(regex_str, replace, string, count=0, flags=0, /)",
        new="""
def sub(
   regex_str: _StrLike, 
   replace: AnyStr | Callable[["Match[AnyStr]"], AnyStr], 
   string: AnyStr, 
   count: int = 0, 
   flags: int = 0, 
   /,
) -> AnyStr
""",
        indent=0,
    )
    shed.vars(
        old=r".. data:: DEBUG", class_var=None,
    )
    # `.. _regex:` is in `rst` file but not rendered by Sphinx (has no description either)!
    # It is ignored along with the `Regex` header in the `rst` file.
    shed.consume_minuses_underline_line(and_preceding_lines=True)

    cmd: Final = r".. method:: "
    shed.class_(
        pre_str="# noinspection PyPep8Naming", name=r"ure", end=cmd,
    )
    shed.defs_with_common_description(
        cmd=cmd,
        old2new={
            r"regex.match(string)": 'def match(self, string: AnyStr, /) -> "Match[AnyStr]"',
            r"regex.search(string)": 'def search(self, string: AnyStr, /) -> "Match[AnyStr]"',
            r"regex.sub(replace, string, count=0, flags=0, /)": """
def sub(
   self, 
   replace: AnyStr | Callable[["Match[AnyStr]"], AnyStr], 
   string: AnyStr, 
   count: int = 0, 
   flags: int = 0, 
   /,
) -> AnyStr
""",
        },
    )
    shed.def_(
        old=r".. method:: regex.split(string, max_split=-1, /)",
        new="def split(self, string: AnyStr, max_split: int = -1, /) -> list[AnyStr]",
        end="Match objects",
    )

    shed.consume_minuses_underline_line(and_preceding_lines=True)
    shed.class_(
        name=r"Match(Generic[AnyStr])",
        extra_docs=[
            """
   The name, `Match`, used for typing is not the same as the runtime name, `match` (note lowercase `m`).
   The reason for this difference is that the runtime uses `match` as both a class name and as a method name and
   this is not possible within code written entirely in Python and therefore not possible within typing code.
""".strip(
                "\n"
            )
        ],
        end=cmd,
    )
    shed.def_(
        old=r".. method:: match.group(index)",
        new="def group(self, index: int, /) -> AnyStr",
    )
    shed.def_(
        old=r".. method:: match.groups()",
        new="def groups(self) -> tuple[AnyStr | Any, ...]",
    )
    shed.defs_with_common_description(
        cmd=r".. method:: ",
        old2new={
            r"match.start([index])": "def start(self, index: int = ..., /) -> int",
            r"match.end([index])": "def end(self, index: int = ..., /) -> int",
        },
    )
    shed.def_(
        old=r".. method:: match.span([index])",
        new="def span(self, index: int = ..., /) -> tuple[int, int]",
    )

    shed.write(u_also=True)
