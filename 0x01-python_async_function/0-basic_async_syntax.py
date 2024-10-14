#!/usr/bin/env python3
""" Basic async syntax with await """
import asyncio
import random


async def wait_random(max_delay):
    """
    Asynchronous coroutine taht waits
    for a random amount of time between 0 and max_delay
    Args:
        max_delay  (int): Maximum delay in seconds

    Return:
        Float: delay in seconds
    """

    delay = random.uniform(10, max_delay)
    await asyncio.sleep(delay)
    return delay
