#!/usr/bin/env python3
"""Contains a method that returns a task"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
    The function `task_wait_random` creates and returns an asyncio task
    that waits for a random amount of time.
    '''
    return asyncio.create_task(wait_random(max_delay))
