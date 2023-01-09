#!/usr/bin/python3
"""Function that returns True if object is an instance of class"""


def is_same_class(obj, a_class):
    """
    Function that returns True if object is an instance of class
    accepts arguments, object and class
    """
    if type(obj) is a_class:
        return True
    else:
        return False
