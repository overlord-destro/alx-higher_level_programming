#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newdict = {}
    for keys, vals in a_dictionary.items():
        newdict.setdefault(keys, vals * 2)
    return newdict
