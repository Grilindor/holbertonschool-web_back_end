#!/usr/bin/env python3
""" 1. Async Comprehensions """
import asyncio
import typing
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """
    Returns a list of values from async_generator using asynchronous
    comprehension.
    This function collects and returns all values yielded by the
    async_generator function in a list, processed asynchronously.
    """
    return [i async for i in async_generator()]
