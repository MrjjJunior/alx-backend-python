#!/usr/bin/env python3
""" Basic async syntax with await """
import asyncio
import random


async def wait_random(max_delay):
    """ Asynchronous coroutine taht waits """

    delay = random.uniform(10, max_delay)
    await asyncio.sleep(delay)
    return delay
