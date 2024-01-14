#!/usr/bin/env python3
'''
The `wait_n` function takes in two parameters, `n` and `max_delay`, and
returns a list of `n` random delay times.
'''
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    The `wait_n` function takes in two parameters, `n` and `max_delay`,
    and returns a list of `n` random delay times.
    '''
    task = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await t for t in asyncio.as_completed(task)]
