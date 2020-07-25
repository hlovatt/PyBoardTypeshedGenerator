from dataclasses import dataclass, field
from typing import Iterator, List, Union
from urllib.request import urlopen, Request

__author__      = "Howard C Lovatt"
__copyright__   = "Howard C Lovatt, 2020 onwards."
__license__     = "MIT https://opensource.org/licenses/MIT (as used by MicroPython)."
__version__     = "0.0.0"


@dataclass
class Lines(Iterator[str]):
    _lines: List[str] = field(default_factory=list)

    def __iter__(self) -> 'Lines':
        return self

    def __next__(self) -> str:
        if not self._lines:
            raise StopIteration  # Should really remember that it has stopped and then stay stopped, but it doesn't!
        return self._lines.pop()

    def __len__(self):
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
