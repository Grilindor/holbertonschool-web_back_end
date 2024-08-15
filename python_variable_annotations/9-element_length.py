#!/usr/bin/env python3
""" 9. Let's duck type an iterable object """
from typing import Tuple, Sequence, Iterable, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Annotate the function’s parameters and return
    values with appropriate type"""
    return [(i, len(i)) for i in lst]
