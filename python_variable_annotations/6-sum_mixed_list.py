#!/usr/bin/env python3
"""mixed list function"""

from typing import Union


def sum_mixed_list(mxd_lst: list[Union[int, float]]) -> float:
    """sum of mixed numbers"""
    return sum(mxd_lst)