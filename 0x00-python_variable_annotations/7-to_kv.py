#!/usr/bin/env python3
from typing import Union, Tuple
""" Return a Tuple """


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Return a tuple """
    v = v * v
    return (k, v)
