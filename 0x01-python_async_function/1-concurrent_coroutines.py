#!/usr/bin/env python3
"""module: working with multiple coroutines"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """spawn an async function several times """
    # result = []
    # for _ in range(n):
    #     output = await asyncio.gather(wait_random(max_delay))
    #     result.extend(output)
    # return result
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
