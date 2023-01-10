#!/usr/bin/python3
"""Function that reads file and prints to stdout"""


def read_file(filename=""):
    """Function to print content of file to stdout"""
    with open(filename, encoding="utf-8") as f:
        outp = f.read()
        print(outp)
