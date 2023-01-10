#!/usr/bin/python3
"""function that  appends string to file, returns number of characters"""


def append_write(filename="", text=""):
    """function appends string to file, returns number of chars"""
    with open(filename, "a", encoding="utf-8") as f:
        num = f.write(text)
    return num
