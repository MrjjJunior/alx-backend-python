#!/usr/bin/env python3
""" Module """

import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    return asyncio.create_task(wait_random(max_delay))
