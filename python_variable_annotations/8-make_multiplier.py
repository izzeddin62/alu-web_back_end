#!/usr/bin/env python3


def make_multiplier(multiplier: float) -> callable:
    """make_multiplier function"""


    def multiply(n: float) -> float:
        """multiply function"""
        return n * multiplier
    return multiply
