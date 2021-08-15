"""
Generate `pyi` from corresponding `rst` docs.
"""
import repdefs
import rst
from rst2pyi import RST2PyI

__author__ = rst.__author__
__copyright__ = rst.__copyright__
__license__ = rst.__license__
__version__ = "5.0.3"  # Version set by https://github.com/hlovatt/tag2ver


def uasyncio(shed: RST2PyI) -> None:
    shed.module(
        name='uasyncio',
        old='asynchronous I/O scheduler for writing concurrent code',
        post_doc=f'''
from abc import ABC
from typing import Awaitable, TypeVar, Optional, List, Tuple, Union, Callable
from typing import Coroutine, Any, Dict, Iterable, Generic

from uarray import array

_T = TypeVar("_T")
_C = Union[Coroutine[Any, None, _T], Awaitable[_T]]  # `Coroutine` `_T` is covariant and `Awaitable` `_T` is invariant.

{repdefs.AnyReadableBuf}
''',
        end='Core functions',
    )
    shed.def_(
        old='.. function:: create_task(coro)',
        new='def create_task(coro: _C, /) -> Task[_T]',
        indent=0,
    )
    shed.def_(
        old='.. function:: current_task()',
        new='def current_task() -> Optional[Task[Any]]',
        indent=0,
    )
    shed.def_(
        old='.. function:: run(coro)',
        new='def run(coro: _C, /) -> _T',
        indent=0,
    )
    shed.def_(
        old='.. function:: sleep(t)',
        new='def sleep(t: float) -> Awaitable[None]',
        indent=0,
    )
    shed.def_(
        old='.. function:: sleep_ms(t)',
        new='def sleep_ms(t: int, /) -> Awaitable[None]',
        indent=0,
        end='Additional functions'
    )
    shed.def_(
        old='.. function:: wait_for(awaitable, timeout)',
        new='def wait_for(awaitable: Awaitable[_T], timeout: float, /) -> Awaitable[_T]',
        indent=0,
    )
    shed.def_(
        old='.. function:: wait_for_ms(awaitable, timeout)',
        new='def wait_for_ms(awaitable: Awaitable[_T], timeout: int, /) -> Awaitable[_T]',
        indent=0,
    )
    shed.def_(
        old='.. function:: gather(*awaitables, return_exceptions=False)',
        new='def gather(*awaitable: Awaitable[Any], return_exceptions: bool = False) -> Awaitable[List[Any]]',
        indent=0,
        end='class Task',
    )
    task = '.. class:: Task()'
    shed.class_(name='Task(Awaitable[_T], Iterable[_T], Generic[_T], ABC)', end=task)
    shed.def_(
        old=task,
        new='def __init__(self)',
    )
    shed.def_(
        old='.. method:: Task.cancel()',
        new='def cancel(self) -> None',
        end='class Event',
    )
    event = '.. class:: Event()'
    shed.class_(name='Event', end=event)
    shed.def_(
        old=event,
        new='def __init__(self)',
    )
    shed.def_(
        old='.. method:: Event.is_set()',
        new='def is_set(self) -> bool',
    )
    shed.def_(
        old='.. method:: Event.set()',
        new='def set(self) -> None',
    )
    shed.def_(
        old='.. method:: Event.clear()',
        new='def clear(self) -> None',
    )
    shed.def_(
        old='.. method:: Event.wait()',
        new='def wait(self) -> Awaitable[Any]',
        end='class ThreadSafeFlag',
    )
    thread_safe = '.. class:: ThreadSafeFlag()'
    shed.class_(name='ThreadSafeFlag', end=thread_safe)
    shed.def_(
        old=thread_safe,
        new='def __init__(self)',
    )
    shed.def_(
        old='.. method:: ThreadSafeFlag.set()',
        new='def set(self) -> None',
    )
    shed.def_(
        old='.. method:: ThreadSafeFlag.wait()',
        new='def wait(self) -> Awaitable[None]',
        end='class Lock',
    )
    lock = '.. class:: Lock()'
    shed.class_(name='Lock(Awaitable[None], ABC)', end=lock)
    shed.def_(
        old=lock,
        new='def __init__(self)',
    )
    shed.def_(
        old='.. method:: Lock.locked()',
        new='def locked(self) -> bool',
    )
    shed.def_(
        old='.. method:: Lock.acquire()',
        new='def acquire(self) -> Awaitable[None]',
    )
    shed.def_(
        old='.. method:: Lock.release()',
        new='def release(self) -> None',
        end='TCP stream connections',
    )
    shed.def_(
        pre_str='''
StreamReader = 'Stream'

StreamWriter = 'Stream'
''',
        old='.. function:: open_connection(host, port)',
        new='''
def open_connection(
   host: Optional[str], 
   port: Union[str, int, None],
   /,
) -> Awaitable[Tuple[StreamReader, StreamWriter]]
''',
        indent=0,
    )
    shed.def_(
        old='.. function:: start_server(callback, host, port, backlog=5)',
        new='''
def start_server(
   callback: Callable[[StreamReader, StreamWriter], None], 
   host: Optional[str], 
   port: Union[str, int, None],
   backlog: int = 5, 
   /,
) -> Awaitable["Server"]
''',
        indent=0,
    )
    stream = '.. class:: Stream()'
    shed.class_(name='Stream', end=stream)
    shed.def_(
        old=stream,
        new='def __init__(self)',
    )
    shed.def_(
        old='.. method:: Stream.get_extra_info(v)',
        new='def get_extra_info(self, v: str, /) -> str',
    )
    shed.def_(
        old='.. method:: Stream.close()',
        new='def close(self) -> None',
    )
    shed.def_(
        old='.. method:: Stream.wait_closed()',
        new='def wait_close(self) -> Awaitable[None]',
    )
    shed.def_(
        old='.. method:: Stream.read(n)',
        new='def read(self, n: int, /) -> Awaitable[bytes]',
    )
    shed.def_(
        old='.. method:: Stream.readline()',
        new='def readline(self) -> Awaitable[bytes]',
    )
    shed.def_(
        old='.. method:: Stream.write(buf)',
        new='def write(self, buf: _AnyReadableBuf, /) -> None',
    )
    shed.def_(
        old='.. method:: Stream.drain()',
        new='def drain(self) -> Awaitable[None]',
    )
    server = '.. class:: Server()'
    shed.class_(name='Server', end=server)
    shed.def_(
        old=server,
        new='def __init__(self)',
    )
    shed.def_(
        old='.. method:: Server.close()',
        new='def close(self) -> None',
    )
    shed.def_(
        old='.. method:: Server.wait_closed()',
        new='def wait_close(self) -> Awaitable[None]',
        end='Event Loop',
    )
    shed.def_(
        old='.. function:: get_event_loop()',
        new='def get_event_loop() -> "Loop"',
        indent=0,
    )
    shed.def_(
        old='.. function:: new_event_loop()',
        new='def new_event_loop() -> "Loop"',
        indent=0,
    )
    loop = '.. class:: Loop()'
    shed.class_(name='Loop', end=loop)
    shed.def_(
        old=loop,
        new='def __init__(self)',
    )
    shed.def_(
        old='.. method:: Loop.create_task(coro)',
        new='def create_task(self, coro: _C, /) -> Task[_T]',
    )
    shed.def_(
        old='.. method:: Loop.run_forever()',
        new='def run_forever(self) -> None',
    )
    shed.def_(
        old='.. method:: Loop.run_until_complete(awaitable)',
        new='def run_until_complete(self, awaitable: Awaitable[_T], /) -> None',
    )
    shed.def_(
        old='.. method:: Loop.stop()',
        new='def stop(self) -> None',
    )
    shed.def_(
        old='.. method:: Loop.close()',
        new='def close(self) -> None',
    )
    shed.def_(
        old='.. method:: Loop.set_exception_handler(handler)',
        new='def set_exception_handler(self, handler: Optional[Callable[["Loop", Dict[str, Any]], None]], /) -> None',
    )
    shed.def_(
        old='.. method:: Loop.get_exception_handler()',
        new='def get_exception_handler(self) -> Optional[Callable[["Loop", Dict[str, Any]], None]]',
    )
    shed.def_(
        old='.. method:: Loop.default_exception_handler(context)',
        new='def default_exception_handler(self, context: Dict[str, Any], /) -> None',
    )
    shed.def_(
        old='.. method:: Loop.call_exception_handler(context)',
        new='def call_exception_handler(self, context: Dict[str, Any], /) -> None',
    )
    shed.write()
