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
__version__ = "7.3.0"  # Version set by https://github.com/hlovatt/tag2ver


def stm(shed: RST2PyI) -> None:
    shed.module(
        name="stm",
        old="functionality specific to STM32 MCUs",
        post_doc='''
from typing import Final

# noinspection PyPep8Naming
class mem:
    """
    Memory objects that can be used in combination with the peripheral register
    constants to read and write registers of the MCU hardware peripherals, as well
    as all other areas of address space.
    
    Cannot make an instance of this class,
    but pre-made instances: `mem8`, `mem16`, and `mem32` are available for 8, 16, and 32 bit access respectively.
    """
    
    def __getitem__(self, loc: int, /) -> int:
        """
        Get the contents of the given memory location using subscript notation e.g., `mem8[0]`.
        Returns 8 bits for mem8`, 16 bits for `mem16`, and 32 bits for `mem32`, in all cases as a single `int`.
        Location doesn't overflow, it is truncated.
        
        Can be used in combination with the peripheral register
        constants to read registers of the MCU hardware peripherals, as well
        as all other areas of address space.
        """
    
    def __setitem__(self, loc: int, value: int, /) -> None:
        """
        Set the contents of the given memory location to the given value using subscript notation e.g., `mem8[0] = 195`.
        Sets 8 bits for `mem8`, 16 bits for `mem16`, and 32 bits for `mem32`, from the given `int` value.
        Location doesn't overflow, it is truncated.
        
        Can be used in combination with the peripheral register
        constants to write registers of the MCU hardware peripherals, as well
        as all other areas of address space.
        """
''',
        end="Memory access",
    )

    shed.consume_containing_line(
        "The module exposes three objects used for raw memory access.",
        and_preceding_lines=True,
    )
    shed.vars(
        old=r".. data:: mem8", class_var=None, type_="mem",
    )
    shed.vars(
        old=r".. data:: mem16", class_var=None, type_="mem",
    )
    use_sub: Final = "Use subscript notation ``[...]`` to index these objects with the address of"
    shed.vars(
        old=r".. data:: mem32", class_var=None, type_="mem", end=use_sub,
    )

    shed.consume_containing_line(
        use_sub, and_preceding_lines=True,
    )
    shed.consume_containing_line(
        "interest.", and_preceding_lines=True,
    )
    shed.consume_containing_line(
        "These memory objects can be used in combination with the peripheral register",
        and_preceding_lines=True,
    )
    shed.consume_containing_line(
        "constants to read and write registers of the MCU hardware peripherals, as well",
        and_preceding_lines=True,
    )
    shed.consume_containing_line(
        "as all other areas of address space.", and_preceding_lines=True,
    )
    shed.consume_minuses_underline_line(and_preceding_lines=True)

    gpioa_reg = r".. data:: GPIOA"
    extra_reg_doc: Final = strip_leading_and_trailing_blank_lines(
        shed.extra_docs(indent=0, end=gpioa_reg,)
    )
    temp_reg_def: Final = shed.rst.pop_lines(num_lines=21)
    fun_spec: Final = "Functions specific to STM32WBxx MCUs"
    extra_reg_doc.extend(
        strip_leading_and_trailing_blank_lines(shed.extra_docs(indent=0, end=fun_spec))
    )
    shed.rst.push_lines(lines=temp_reg_def)
    shed.vars(
        old=gpioa_reg, class_var=None, extra_docs=extra_reg_doc,
    )
    shed.vars(
        old=r".. data:: GPIOB", class_var=None, extra_docs=extra_reg_doc,
    )
    shed.vars(
        old=r".. data:: GPIO_BSRR", class_var=None, extra_docs=extra_reg_doc,
    )
    shed.vars(
        old=r".. data:: GPIO_IDR", class_var=None, extra_docs=extra_reg_doc,
    )
    shed.vars(
        old=r".. data:: GPIO_ODR",
        class_var=None,
        extra_docs=extra_reg_doc,
        end=fun_spec,
    )

    shed.consume_minuses_underline_line(and_preceding_lines=True)
    rf_stat = r".. function:: rfcore_status()"
    fun_spec_extra_doc: Final = strip_leading_and_trailing_blank_lines(
        shed.extra_docs(end=rf_stat)
    )
    shed.def_(
        old=rf_stat,
        new="def rfcore_status() -> int",
        indent=0,
        extra_docs=fun_spec_extra_doc,
    )
    shed.def_(
        old=r".. function:: rfcore_fw_version(id)",
        new="def rfcore_fw_version(id: int, /) -> tuple[int, int, int, int, int]",
        indent=0,
        extra_docs=fun_spec_extra_doc,
    )
    make_room: Final = shed.rst.pop_lines(num_lines=5)
    dummy_end = "DUMMY END LINE"
    shed.rst.push_line(dummy_end)
    shed.rst.push_lines(lines=make_room)
    shed.def_(
        old=r".. function:: rfcore_sys_hci(ogf, ocf, data, timeout_ms=0)",
        new="def rfcore_sys_hci(ogf: int, ocf: int, data: int, timeout_ms: int = 0, /) -> bytes",
        indent=0,
        extra_docs=fun_spec_extra_doc,
        end=dummy_end,
    )
    shed.consume_containing_line(dummy_end)

    shed.write()
