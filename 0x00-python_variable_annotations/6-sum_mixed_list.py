#!/usr/bin/env python3
from typing import List, Union
"""
code starts here
"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    The function `sum_mixed_list` takes a list of integers and floats as
    input and returns the sum of all the elements in the list.
    """
    result = 0
    for i in mxd_lst:
        result += i
    return result
