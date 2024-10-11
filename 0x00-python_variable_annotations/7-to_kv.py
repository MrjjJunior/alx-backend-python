#!/usr/bin/env python3
from typing import Union, Tuple
""" Tuple Returs a squared number """


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Return a tuple with a square number"""
    return (k, float(v * v))
