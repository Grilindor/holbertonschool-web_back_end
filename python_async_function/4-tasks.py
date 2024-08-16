#!/usr/bin/env python3
""" 4. Tasks """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ asyncronique function to creat a list of float
    using task_wait_random for n use """
    listing = [task_wait_random(max_delay) for _ in range(n)]

    delays = await asyncio.gather(*listing)

    """ sort the result without sort() """
    for i in range(len(delays)):
        for j in range(i + 1, len(delays)):
            if delays[i] > delays[j]:
                delays[i], delays[j] = delays[j], delays[i]

    return delays
