#!/usr/bin/env python3
"""module: duck type"""
from typing import List, Sequence, Tuple, Iterable

Lists = Iterable[Sequence]
Rtn = List[Tuple[Sequence, int]]


def element_length(lst: Lists) -> Rtn:
    """Returns an iterable and its length"""
    return [(i, len(i)) for i in lst]
