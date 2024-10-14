#!/usr/bin/env python3
"""module: working with multiple coroutines"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """spawn an async function several times """
    # result = []
    # for _ in range(n):
    #     output = await asyncio.gather(wait_random(max_delay))
    #     result.extend(output)
    # return sorted(result)
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
