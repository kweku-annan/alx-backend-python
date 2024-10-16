#!/usr/bin/env python3
"""Executes multiple coroutines at the same time with async"""


import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random n times and returns a list of delays"""
    task: List[float] = await asyncio.gather(*(
        task_wait_random(max_delay) for _ in range(n)))
    sorted_task = sorted(task)
    return sorted_task
