#!/usr/bin/env python3
"""module: duck typing annotation"""
from typing import Sequence, Any, Union

type NoneType = None
Lists = Sequence[Any]
Rtn = Union[Any, NoneType]


def safe_first_element(lst: Lists) -> Rtn:
    """Duck typing annotations"""
    if lst:
        return lst[0]
    return None
