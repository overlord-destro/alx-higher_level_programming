#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    temp = 0
    for k, v in a_dictionary.items():
        if v > temp:
            temp = v
            name = k
    return name
