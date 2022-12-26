#!/usr/bin/python3
"""a function that adds 2 integers"""


def add_integer(a, b=98):
    """adds 2 integers, must be float or integer input"""
    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
