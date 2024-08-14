#!/usr/bin/env python3
""" 7. Complex types - string and int/float to tuple """
from typing import Tuple, Union


def to_kv(k: str, v: Union[float, int]) -> Tuple[str, float]:
    """ return str k and the square float of v """
    return k, float(v ** 2)
