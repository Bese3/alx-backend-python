#!/usr/bin/env python3
from typing import Callable
"""
code starts here
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    The function "make_multiplier" returns a new function that multiplies a
    given number by a specified multiplier."""
    def new_mult(m: float) -> float:
        return multiplier * m
    return new_mult
