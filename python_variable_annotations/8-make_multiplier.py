#!/usr/bin/env python3
""" 8. Complex types - functions """
from typing import Callable


""" the Callable function will make the 1e function in wait
for the second function """


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ create anoter function to multiple a float with multiplier """
    def multi_funct(x: float) -> float:
        return x * multiplier
    """ return the result of the second function """
    return multi_funct
