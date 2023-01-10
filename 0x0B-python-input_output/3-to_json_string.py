#!/usr/bin/python3
"""function that returns JSON rep of a string"""


import json


def to_json_string(my_obj):
    """returns json rep of a string"""
    return json.dumps(my_obj)
