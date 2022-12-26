#!/usr/bin/python3
""" Function that prints sentence with first name last name"""


def say_my_name(first_name, last_name=""):
    """ accepts first name and/or last name, they must be strings"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
