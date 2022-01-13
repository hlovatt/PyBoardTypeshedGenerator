from dataclasses import dataclass, field
from typing import Iterator, List, Final, Union
from urllib.request import urlopen, Request

__author__ = "Howard C Lovatt"
__copyright__ = "Howard C Lovatt, 2020 onwards."
__license__ = "MIT https://opensource.org/licenses/MIT (as used by MicroPython)."
__version__ = "7.5.0"  # Version set by https://github.com/hlovatt/tag2ver


@dataclass(frozen=True)
class RST(Iterator[str]):
    """
    An iterator of lines, used to read in the restructured text, `.rst`, files.
    `RST` works like a stack, you `push_line`s or `push_url`s (whole files) and then pop them using `next`
    (typically via a `for` loop).
    `push_line` and `push_lines` are typically used to provide 'push back' when parsing.
    `__len__` is provided and is typically use to test if empty, via implicit bool conversion.
    `peek` is useful for debugging parsers.
    `pop_line` and `pop_lines` are useful for fixing up `rst` files to make them easier to parse.
    """

    _lines: Final[List[str]] = field(default_factory=list)

    def __iter__(self) -> "RST":
        return self

    def __next__(self) -> str:
        if not self._lines:
            # Should really (`Iterator` contract) remember that it has stopped and then stay stopped;
            # but it doesn't, in fact it does the opposite and is reused via `Typeshed` instance for the next module!
            raise StopIteration
        return self._lines.pop()

    def __len__(self) -> int:
        return len(self._lines)

    def push_line(self, line: str) -> None:
        self._lines.append(line)

    def push_lines(self, *, lines: List[str]) -> None:
        self._lines.extend(reversed(lines))

    def push_url(self, url: Union[str, Request]) -> None:
        with urlopen(url) as f:
            lines = f.read().splitlines()
        for line in reversed(lines):
            self._lines.append(line.decode())

    def peek(self) -> str:
        if not self._lines:
            return "No more lines!"
        return self._lines[-1]

    def pop_line(self) -> str:
        return self._lines.pop()

    def pop_lines(self, *, num_lines: int) -> List[str]:
        lines: List[str] = []
        for _ in range(num_lines):
            lines.append(self._lines.pop())
        return lines
