#!/usr/bin/env python3
""" Function that imports code from prev file """
import asyncio
import importlib
from typing import List

basic_async_syntax = importlib.import_module('0-basic_async_syntax')
wait_random = basic_async_syntax.wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """  Function that waits n times with random delay """

    wait_times = await asyncio.gather(
        *tuple(map(lambda _:
        wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)

'''
from random import uniform

async def wait_n(n:int, max_delay:int) -> List[float]:
    pass
'''
