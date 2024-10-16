#!/usr/bin/env python3
"""This task is about the basic syntax of async"""

import random
import asyncio
from typing import Awaitable


async def wait_random(max_delay: int = 10) -> Awaitable[float]:
    """Takes an integer argument, generates and return float"""
    number = random.uniform(0, max_delay)
    await asyncio.sleep(number)
    return number
