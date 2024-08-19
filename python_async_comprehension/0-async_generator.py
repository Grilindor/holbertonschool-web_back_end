#!/usr/bin/env python3
""" 0. Async Generator """
import asyncio
import random


async def async_generator():
    """ wait 1sec befor excut random nummber and return it """
    for i in range(10):
        await asyncio.sleep(1)
        a = random.uniform(0, 10)
        yield a
