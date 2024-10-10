#!/usr/bin/env python3
""" Annotation """
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable) -> List[Tuple[Sequence, int]]:
    """  Returns values with the appropriate types """
    return [(i, len(i)) for i in lst]
