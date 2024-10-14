#!/usr/bin/env python3
""" Function that imports code from prev file """
import asyncio
import random
from typing import List


async def wait_random(max_delay: int) -> float:
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

async def wait_n(n: int, max_delay: int) -> list:
    """ Create a list of tasks using wait_random """
    tasks = [wait_random(max_delay) for _ in range(n)]
    
    # Use asyncio.as_completed to get the results in the order they finish
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    
    return delays
