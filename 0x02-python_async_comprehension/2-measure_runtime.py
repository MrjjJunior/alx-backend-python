#!/usr/bin/env python3
""" This module contains the function """
import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """  This function measures the runtime of a given function """
    start_time = time.perf_counter()  # Start measuring time

    # Run async_comprehension 4 times concurrently
    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_time = time.perf_counter()  # End measuring time
    total_runtime = end_time - start_time  # Calculate the total runtime

    return total_runtime
