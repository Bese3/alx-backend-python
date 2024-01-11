#!/usr/bin/env python3
from typing import Tuple, Union
"""
code starts here
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    The function takes a key (k) and a value (v) and returns a tuple
    with the key and the square of the value.
    """
    return (k, float(v**2))
