#!/usr/bin/env python3
""" Function that imports code from prev file """
import asyncio
import random
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Create a list of tasks using wait_random """
    tasks = [wait_random(max_delay) for _ in range(n)]

    # Use asyncio.as_completed to get the results in the order they finish
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
