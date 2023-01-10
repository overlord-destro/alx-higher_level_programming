#!/usr/bin/python3
"""function that writes a string to text file, returns number of characters"""


def write_file(filename="", text=""):
    """function writes string to file, returns number of chars"""
    with open(filename, "w", encoding="utf-8") as f:
        num = f.write(text)
    return num
