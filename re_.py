"""
Generate `pyi` from corresponding `rst` docs.
"""
from typing import Final

import rst
from rst2pyi import RST2PyI

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = "6.1.0"  # Version set by https://github.com/hlovatt/tag2ver


def re(shed: RST2PyI) -> None:
    shed.module(
        name='re',
        old='regular expressions',
        post_doc=f'''
from typing import AnyStr, Callable, Generic, Tuple, Final, Any

_StrLike = str | bytes
''',
        end='Functions',
    )

    shed.def_(
        old=R'.. function:: compile(regex_str, [flags])',
        new='def compile(regex_str: _StrLike, flags: int = ..., /) -> "ure"',
        indent=0,
    )
    shed.def_(
        old=R'.. function:: match(regex_str, string)',
        new='def match(regex_str: _StrLike, string: AnyStr, /) -> "Match[AnyStr]"',
        indent=0,
    )
    shed.def_(
        old=R'.. function:: search(regex_str, string)',
        new='def search(regex_str: _StrLike, string: AnyStr, /) -> "Match[AnyStr]"',
        indent=0,
    )
    shed.def_(
        old=R'.. function:: sub(regex_str, replace, string, count=0, flags=0, /)',
        new='''
def sub(
   regex_str: _StrLike, 
   replace: AnyStr | Callable[["Match[AnyStr]"], AnyStr], 
   string: AnyStr, 
   count: int = 0, 
   flags: int = 0, 
   /,
) -> AnyStr
''',
        indent=0,
    )
    shed.vars(
        old=R'.. data:: DEBUG',
        class_var=None
    )
    # `.. _regex:` is in `rst` file but not rendered by Sphinx (has no description either)!
    # It is ignored along with the `Regex` header in the `rst` file.
    shed.consume_header_line(and_preceding_lines=True)

    cmd: Final = R'.. method:: '
    shed.class_(
        pre_str='# noinspection PyPep8Naming',
        name=R'ure',
        end=cmd,
    )
    shed.defs_with_common_description(
        cmd=cmd,
        old2new={
            R'regex.match(string)':
                'def match(self, string: AnyStr, /) -> "Match[AnyStr]"',
            R'regex.search(string)':
                'def search(self, string: AnyStr, /) -> "Match[AnyStr]"',
            R'regex.sub(replace, string, count=0, flags=0, /)':
                '''
def sub(
   self, 
   replace: AnyStr | Callable[["Match[AnyStr]"], AnyStr], 
   string: AnyStr, 
   count: int = 0, 
   flags: int = 0, 
   /,
) -> AnyStr
''',
        }
    )
    shed.def_(
        old=R'.. method:: regex.split(string, max_split=-1, /)',
        new='def split(self, string: AnyStr, max_split: int = -1, /) -> list[AnyStr]',
        end='Match objects'
    )

    shed.consume_header_line(and_preceding_lines=True)
    shed.class_(
        name=R'Match(Generic[AnyStr])',
        extra_docs=[
'''   The name, `Match`, used for typing is not the same as the runtime name, `match` (note lowercase `m`).
   The reason is that the runtime uses `match` as both a class name and as a method name and
   this is not possible within code written entirely in Python and therefore not possible within typing code.'''
        ],
        end=cmd,
    )
    shed.def_(
        old=R'.. method:: match.group(index)',
        new='def group(self, index: int, /) -> AnyStr',
    )
    shed.def_(
        old=R'.. method:: match.groups()',
        new='def groups(self) -> Tuple[AnyStr | Any, ...]',
    )
    shed.defs_with_common_description(
        cmd=R'.. method:: ',
        old2new={
            R'match.start([index])':
                'def start(self, index: int = ..., /) -> int',
            R'match.end([index])':
                'def end(self, index: int = ..., /) -> int',
        },
    )
    shed.def_(
        old=R'.. method:: match.span([index])',
        new='def span(self, index: int = ..., /) -> Tuple[int, int]',
    )

    shed.write(u_also=True)
