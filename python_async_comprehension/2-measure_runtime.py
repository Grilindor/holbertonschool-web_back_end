#!/usr/bin/env python3
""" 2. Run time for four parallel comprehensions """
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime of running async_comprehension
    four times in parallel.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time.perf_counter()
    total_time = end_time - start_time
    return total_time
