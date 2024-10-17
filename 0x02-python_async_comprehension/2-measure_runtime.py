#!/usr/bin/env python3
"""Contains a coroutine that measures the runtime of another"""
import asyncio
import time
async_compre = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Returns the runtime of a coroutine"""
    start_time = time.perf_counter()
    await asyncio.gather(*(async_compre() for _ in range(3)))
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    return elapsed_time
