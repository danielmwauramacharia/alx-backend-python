#!/usr/bin/env python3
"""module: Type Checking"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Type checking"""
    return [
        item for item in lst
        for i in range(factor)
    ]


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
