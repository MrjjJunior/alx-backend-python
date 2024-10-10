#!/usr/bin/env python3
""" Given parameters """
from typing import Union, Mapping, Any, TypeVar

T = TypeVar('T')
r = Union[Any, T]


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None]) -> r:
    """ add type annotations to the function """
    if key in dct:
        return dct[key]
    else:
        return default
