#!/usr/bin/env python3
"""module: function elements to a tuple"""
from typing import Tuple, Union

Vars = Union[int, float]
Tuples = Tuple[str, float]


def to_kv(k: str, v: Vars) -> Tuples:
    """Return a tuple of str, float"""
    sq: float = v ** 2
    return (k, sq)
