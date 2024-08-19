#!/usr/bin/env python3
""" 0. Simple helper function """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    param page: begin at page 1
    param page_size: number of element in one page

    return a Tuple with start_index, end_index
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
