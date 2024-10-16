#!/usr/bin/env python3
"""module: More on annotationns"""
from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None]) -> Union[Any, T]:
    """More involved type annotations"""
    if key in dct:
        return dct[key]
    return default
