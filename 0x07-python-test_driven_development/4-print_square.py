#!/usr/bin/python3
"""A function that prints a square with the character #"""


def print_square(size):
    """
    accepts size which must be integer and prints square
    using #
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
