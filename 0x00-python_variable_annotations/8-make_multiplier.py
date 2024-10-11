#!/usr/bin/env python3
"""module: complex type function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function"""
    def mult(num: float) -> float:
        return num * multiplier

    return mult
