import asyncio
import time
import traceback
from .elements.element import Element
from .utils import handle_exceptions

class Timer:

    tasks = []

    def __init__(self, interval, callback, *, once=False):
        """Timer

        One major drive behind the creation of NiceGUI was the necessity to have an simple approach to update the interface in regular intervals. For example to show a graph with incomming measurements.

        :param interval: the interval in which the timer is been called
        :param callback: function to execute when interval elapses
        :param once: weather the callback is only executed once after an delay specified by `interval`; default is False
        """

        parent = Element.view_stack[-1]

        async def timeout():

            await asyncio.sleep(interval)
            handle_exceptions(callback)()
            await parent.update()

        async def loop():

            while True:
                try:
                    start = time.time()
                    handle_exceptions(callback)()
                    await parent.update()
                    dt = time.time() - start
                    await asyncio.sleep(interval - dt)
                except:
                    traceback.print_exc()
                    await asyncio.sleep(interval)

        self.tasks.append(timeout() if once else loop())
