#!/usr/bin/env python3
"""
The `measure_runtime` function measures the runtime of an asynchronous
comprehension in Python.
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    The `measure_runtime` function measures the runtime of
    an asynchronous comprehension in Python.
    """
    b = time.perf_counter()
    task = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*task)
    now = time.perf_counter() - b
    return now
