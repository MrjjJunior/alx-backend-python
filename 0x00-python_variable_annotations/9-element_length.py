#!/usr/bin/python3
"""  """
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable) -> List[Tuple[Sequence, int]]:
    """  """
    return [(i, len(i)) for i in lst]
