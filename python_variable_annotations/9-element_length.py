#!/usr/bin/env python3
"""element length function"""
from typing import List, Tuple, Sequence


def element_length(lst: List[str]) -> List[Tuple[Sequence, int]]:
    """return a list with a string and number"""
    return [(i, len(i)) for i in lst]
