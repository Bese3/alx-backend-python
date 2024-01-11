#!/usr/bin/env python3
from typing import Iterator, Sequence, List, Tuple
"""
code starts here
"""


def element_length(lst: Iterator[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    The function `element_length` takes an iterator of sequences as input
    and returns a list of tuples, where each tuple contains a sequence
    from the input and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
