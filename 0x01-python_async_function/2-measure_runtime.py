#!/usr/bin/env python3
""" A Python Module """
import asyncio, importlib, time 

#concurrent_coroutines = importlib.import_module('0-basic_async_syntax')
#wait_n = concurrent_coroutines.wait_n
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """sumary_line
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    
    start_time =  time.time()

    asyncio.run(wait_n(n, max_delay))
    return  ((time.time() - start_time) / n)

