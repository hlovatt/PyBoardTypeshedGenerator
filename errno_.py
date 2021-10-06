"""
Generate `pyi` from corresponding `rst` docs.
"""

import rst
from rst2pyi import RST2PyI

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = "6.2.1"  # Version set by https://github.com/hlovatt/tag2ver


def errno(shed: RST2PyI) -> None:
    shed.module(
        name='errno',
        old='system error codes',
        post_doc=f'''
from typing import Final, Dict
''',
        end=R'Constants',
    )
    shed.vars(
        old=R'.. data:: EEXIST, EAGAIN, etc.',
        class_var=None,
    )
    shed.vars(
        old=R'.. data:: errorcode',
        type_='Dict[int, str]',
        class_var=None,
    )
    shed.write(u_also=True)
