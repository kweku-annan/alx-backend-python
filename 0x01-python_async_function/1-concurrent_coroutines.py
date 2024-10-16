#!/usr/bin/env python3
"""Executes multiple coroutines at the same time with async"""


import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """Spawns wait_random n times and returns a list of delays"""
    task: list = await asyncio.gather(*(
        wait_random(max_delay) for _ in range(n)))
    return task
