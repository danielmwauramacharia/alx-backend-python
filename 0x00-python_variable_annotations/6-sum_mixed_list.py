#!/usr/bin/env python3
"""module: takes mixed list and return sum as float"""
from typing import List, Union

Mlist = List[Union[int, float]]


def sum_mixed_list(mxd_lst: Mlist) -> float:
    """Returns sum of a mixed lists as a float"""
    return sum(mxd_lst)
