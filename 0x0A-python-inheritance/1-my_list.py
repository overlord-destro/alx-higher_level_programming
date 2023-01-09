#!/usr/bin/python3
"""Class that inherits from list"""


class MyList(list):
    """subclass of the class list"""


    def print_sorted(self):
        cpy = self.copy()
        cpy.sort()
        print(cpy)
