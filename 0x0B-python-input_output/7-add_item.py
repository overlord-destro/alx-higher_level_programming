#!/usr/bin/python3
"""Adds all arguments to a python list and saves to file"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


newlist = []
for i in range(1, len(sys.argv)):
    newlist.append(sys.argv[i])

save_to_json_file(newlist, "add_item.json")
