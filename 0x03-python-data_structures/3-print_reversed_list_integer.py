#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    n = len(my_list) - 1
    while n >= 0:
        print("{:d}".format(my_list[n]))
        n -= 1

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)
