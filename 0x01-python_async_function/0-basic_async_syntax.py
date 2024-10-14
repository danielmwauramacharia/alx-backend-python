#!/usr/bin/env python3
"""
Module: Basic Asyc
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """delay coroutine by the generated time"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
