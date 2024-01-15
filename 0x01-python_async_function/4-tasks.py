#!/usr/bin/env python3
import asyncio
'''
The `task_wait_n` function takes in two parameters, `n` and `max_delay`,
and returns a list of floats
'''
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    The function `task_wait_n` takes in two parameters, `n` and `max_delay`,
    and returns a list of floats.
    '''
    task = [task_wait_random(max_delay) for _ in range(n)]
    return [await t for t in asyncio.as_completed(task)]
