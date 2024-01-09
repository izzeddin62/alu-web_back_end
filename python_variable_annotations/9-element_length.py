#!/usr/bin/env python3
"""element length function"""
from typing import List


def element_length(lst: List[str]) -> List[tuple(str, int)]:
    return [(i, len(i)) for i in lst]