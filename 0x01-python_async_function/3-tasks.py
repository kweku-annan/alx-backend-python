#!/usr/bin/env python3
"""Takes an integer and returns asyncio.Task"""


import asyncio
from typing import TypeVar
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Takes and integer and returns asyncio.Task object"""
    task = asyncio.create_task(wait_random(max_delay))
    return task
