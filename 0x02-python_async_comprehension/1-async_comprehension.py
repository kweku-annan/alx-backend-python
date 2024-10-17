#!/usr/bin/env python3
"""Creates a list using async comprehension for a coroutine"""
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> list:
    """Collects 10 random numbers using an async comprehension"""
    result = [i async for i in async_generator()]
    return result
