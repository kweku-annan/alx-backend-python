#!/usr/bin/env python3
"""This task is about the basic syntax of async"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Takes an integer argument, generates and return float"""
    number: float = random.uniform(0, max_delay)
    await asyncio.sleep(number)
    return number
