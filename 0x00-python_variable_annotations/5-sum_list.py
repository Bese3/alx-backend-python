#!/usr/bin/env python3
from typing import List
"""
code starts here
"""


def sum_list(input_list: List[float]) -> float:
    """
    The function `sum_list` takes a list of floats as input
    and returns the sum of all the elements in the list.
    """
    if input_list is None:
        return 0
    else:
        return float(sum(input_list))
