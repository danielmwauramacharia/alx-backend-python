#!/usr/bin/env python3
"""Module: measure time"""
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Measure the execution time of async function"""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    elapsed = end - start
    average = elapsed / n
    return average
