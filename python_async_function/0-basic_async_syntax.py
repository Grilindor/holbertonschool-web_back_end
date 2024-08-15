#!/usr/bin/env python3
""" 0. The basics of async """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ wait_random waits for a random delay between 0 and max_delay
    (base 10 seconds) """
    wait = random.randint(0, max_delay)
    await asyncio.sleep(wait)
    """ return the value of wait """
    return wait
