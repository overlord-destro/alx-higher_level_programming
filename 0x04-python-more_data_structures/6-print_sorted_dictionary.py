#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary:
        newlist = list(a_dictionary)
        newlist.sort()
        for i in newlist:
            print(i + ": ", a_dictionary[i])
