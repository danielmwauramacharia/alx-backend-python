from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')
Defaults = Union[T]


def safely_get_value(dct: Mapping, key: Any, default: Union[Defaults, None]) -> Union[Any, Defaults]:
    """More involved type annotations"""
    if key in dct:
        return dct[key]
    return default


annotations = safely_get_value.__annotations__

print("Here's what the mappings should look like")
for k, v in annotations.items():
    print(("{}: {}".format(k, v)))
