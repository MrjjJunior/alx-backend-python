#!/usr/bin/env python3
""" Module """
import asyncio
from typing import List

task_wait_random = __import__('1-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """sumary_line
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)