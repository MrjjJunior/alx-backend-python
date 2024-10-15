#!/usr/bin/env python3
""" Python Function """
import asyncio
import random


async def async_generator() -> float:
    """ An async generator """
    for _ in range(10):
        await asyncio.sleep(1)  # Asynchronously wait 1 second
        yield random.uniform(0, 10)  # Yield a random float between 0 and 10
