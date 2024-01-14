#!/usr/bin/env python3
"""
The below function is an asynchronous generator.
"""
import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    The above function is an asynchronous generator that yields random
    float numbers between 0 and 10.
    """
    for _ in range(10):
        rand = uniform(0, 10)
        await asyncio.sleep(1)
        yield rand
