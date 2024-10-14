#!/usr/bin/env python3
""" A Python Module """
import asyncio
import importlib
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Measure the time taken to execute n concurrent coroutines """

    start_time = time.time()

    asyncio.run(wait_n(n, max_delay))
    return ((time.time() - start_time) / n)
