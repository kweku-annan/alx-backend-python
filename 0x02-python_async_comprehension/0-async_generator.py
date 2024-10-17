#!/usr/bin/env python3
"""A coroutine generator that will loop 10 times and wait 1s"""
from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """This will loop 10 asynchronously"""
    for _ in range(10):
        yield (random.uniform(0, 10))
        await asyncio.sleep(1)
