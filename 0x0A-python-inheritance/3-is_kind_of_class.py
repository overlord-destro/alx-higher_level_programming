#!/usr/bin/python3
"""Function that returns true if object is an instance of inherited class"""


def is_kind_of_class(obj, a_class):
    """
    Function that returns true if object is an instance of inherited class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
