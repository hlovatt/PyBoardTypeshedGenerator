from dataclasses import dataclass, field
from typing import Iterator, List, Union
from urllib.request import urlopen, Request

__author__ = "Howard C Lovatt"
__copyright__ = "Howard C Lovatt, 2020 onwards."
__license__ = "MIT https://opensource.org/licenses/MIT (as used by MicroPython)."
__version__ = "3.4.0"  # Version set by https://github.com/hlovatt/tag2ver


@dataclass
class RST(Iterator[str]):
    """
    An iterator of lines, used to read in the restructured text, `.rst`, files.
    `RST` works like a stack, you `push_line`s or `push_url`s (whole files) and then pop them using `next`
    (typically via a `for` loop).
    `push_line` is typically used to provide 'push back' when parsing.
    `__len__` is provided and is typically use to test if empty, via implicit bool conversion.
    `peek` is useful for debugging parsers.
    """
    
    _lines: List[str] = field(default_factory=list)

    def __iter__(self) -> 'RST':
        return self

    def __next__(self) -> str:
        if not self._lines:
            # Should really remember that it has stopped and then stay stopped (`Iterator` contract);
            # but it doesn't, in fact it does the opposite and is reused via `Typeshed` instance for the next module!
            raise StopIteration
        return self._lines.pop()

    def __len__(self) -> int:
        return len(self._lines)

    def push_line(self, line: str) -> None:
        self._lines.append(line)

    def push_url(self, url: Union[str, Request]) -> None:
        with urlopen(url) as f:
            lines = f.read().splitlines()
        for line in reversed(lines):
            self._lines.append(line.decode())

    def peek(self) -> str:
        if not self._lines:
            return 'No more lines!'
        return self._lines[-1]
