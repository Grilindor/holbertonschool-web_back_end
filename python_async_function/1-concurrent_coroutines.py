#!/usr/bin/env python3
""" 1. Let's execute multiple coroutines at the same time with async """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)

"""async def wait_n(n: int, max_delay: int) -> List[float]:
     # asyncronique function to creat a list of float
    using wait_random for n use
    listing = []
    for _ in range(n):
        listing.append(asyncio.create_task(wait_random(max_delay)))

    delays = await asyncio.gather(*listing)

    # sort the result without sort()
    for i in range(len(delays)):
        for j in range(i + 1, len(delays)):
            if delays[i] > delays[j]:
                delays[i], delays[j] = delays[j], delays[i]

    return delays"""
