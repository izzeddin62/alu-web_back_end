#!/usr/bin/env python3
"""make_multiplier function"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable:
    """make_multiplier function"""


    def multiply(n: float) -> float:
        """multiply function"""
        return n * multiplier
    return multiply
