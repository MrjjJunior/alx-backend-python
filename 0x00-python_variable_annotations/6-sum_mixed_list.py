#!/usr/bin/env python3
""" Sum of list """
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Return sum of mixed list """
    return float(sum(mxd_lst))
