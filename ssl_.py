"""
Generate `pyi` from corresponding `rst` docs.
"""
from typing import Final

import rst
from class_ import strip_leading_and_trailing_blank_lines
from rst2pyi import RST2PyI

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = "7.5.2"  # Version set by https://github.com/hlovatt/tag2ver


def ssl(shed: RST2PyI) -> None:
    shed.module(
        name="ssl",
        old="TLS/SSL wrapper for socket objects",
        post_doc=f"""
from typing import Final

from uio import StrOrBytesPath
from usocket import Socket
""",
        end="Functions",
    )

    shed.def_(
        old=(
            r".. function:: ssl.wrap_socket(sock, server_side=False, keyfile=None, certfile=None"
            r", cert_reqs=CERT_NONE, ca_certs=None, do_handshake=True)"
        ),
        new="""
def wrap_socket(
   sock: Socket, 
   server_side: bool = False, 
   keyfile: StrOrBytesPath | None = None, 
   certfile: StrOrBytesPath | None = None,
   cert_reqs: int = "CERT_NONE", 
   ca_certs: str | None = None, 
   do_handshake: bool = True, 
   /,
) -> Socket
""",
        indent=0,
    )
    shed.consume_up_to_but_excl_end_line(end="This exception does NOT exist")
    exception_note: Final = shed.extra_notes(end="Constants",)
    shed.pyi.doc.append(
        """
.. admonition:: Difference to CPython
   :class: attention
The CPython version of ``ssl`` uses ``SSLError``.
""".strip()
    )
    shed.pyi.doc.extend(strip_leading_and_trailing_blank_lines(exception_note))
    shed.consume_minuses_underline_line(and_preceding_lines=True)
    shed.vars(
        old=[".. data:: ssl.CERT_NONE", "ssl.CERT_OPTIONAL", "ssl.CERT_REQUIRED"],
        class_var=None,
    )

    shed.write(u_also=True)
