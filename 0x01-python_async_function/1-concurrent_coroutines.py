#!/usr/bin/env python3
""" A Python module """
import asyncio, importlib
from typing import List

basic_async_syntax = importlib.import_module('0-basic_async_syntax')
wait_random = basic_async_syntax.wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """sumary_line

    Keyword arguments:
    n -- description
    max_delay -- description
    Return: return_description
    """
    
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
