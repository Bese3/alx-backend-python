#!/usr/bin/env python3
"""
`1-async_comprehension` function imports `async_generator` and return List
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    The function `async_comprehension` returns a list of floats obtained
    from an asynchronous generator.
    """
    return [i async for i in async_generator()]
