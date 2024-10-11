#!/usr/bin/env python3
from typing import Union, Tuple
""" a Tuple """


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Return a tuple """
    return (k, float(v * v))
