#!/usr/bin/python3
"""A function that returns attributes of an object"""


def lookup(obj):
    """returns list of attributes of object, accepts object as argument"""
    return list(dir(obj))
