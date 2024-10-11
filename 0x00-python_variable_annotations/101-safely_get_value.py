from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')
Defaults = Union[T]


def safely_get_value(dct: Mapping, key: Any, default: Union[Defaults, None]) -> Union[Any, Defaults]:
    """More involved type annotations"""
    if key in dct:
        return dct[key]
    return default
