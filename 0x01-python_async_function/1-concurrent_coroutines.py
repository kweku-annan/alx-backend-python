#!/usr/bin/env python3
"""Executes multiple coroutines at the same time with async"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random n times and returns a list of delays"""
    task: List[float] = await asyncio.gather(*(
        wait_random(max_delay) for _ in range(n)))
    sorted_task = sorted(task)
    return task
