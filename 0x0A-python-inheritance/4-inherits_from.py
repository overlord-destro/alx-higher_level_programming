#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    function that returns true if object is an instance of class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
