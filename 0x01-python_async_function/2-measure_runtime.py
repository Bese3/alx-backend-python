#!/usr/bin/env python3
'''
The `measure_time` function measures the average time it
takes to execute the `wait_n` function with
a given number of iterations and maximum delay.'''

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    The `measure_time` function measures the average time it takes
    to execute the `wait_n` function with a given number of iterations.
    '''
    b = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    new = time.perf_counter() - b
    return new / n
