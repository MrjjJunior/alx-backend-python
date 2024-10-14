#!/usr/bin/env python3
""" Function that imports code from prev file """
import asyncio
import importlib
from typing import List

wait_random = __import__("0-basic_async_syntax.py").wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """ Function that waits n times and returns a list of delays """

    tasks = [wait_random(max_delay) for _ in range(n)]
    
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    
    return delays
