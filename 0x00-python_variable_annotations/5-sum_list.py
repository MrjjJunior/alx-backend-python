#!/usr/bin/python3
""" Function that return sum of list """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Return the sum of list """
    total = float(sum(input_list))
    return total
