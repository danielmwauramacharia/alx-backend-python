#!/usr/bin/env python3
"""module: duck typing annotation"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Duck typing annotations"""
    if lst:
        return lst[0]
    return None
