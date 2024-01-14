#!/usr/bin/env python3
'''
The `wait_random` function asynchronously waits for a random
amount of time and then returns the delay.
'''
from random import uniform
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    '''
    The `wait_random` function asynchronously waits for a
    random amount of time and then returns the delay.
    '''
    r = uniform(0, max_delay)
    await asyncio.sleep(r)
    return r
