#!/usr/bin/python3
"""Creating a class Square that defines a square"""


class Square:
    """creating a class square"""
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(position) != tuple:
            raise TypeError("posititon must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("posititon must be a tuple of 2 positive integers")
        if type(position[0]) != int or type(position[1]) != int:
            raise TypeError(
                    "posititon must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("posititon must be a tuple of 2 positive integers")

        self.__size = size
        self.__position = position

    def area(self):
        return (self.__size * self.__size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple:
            raise TypeError("posititon must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("posititon must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError(
                    "posititon must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("posititon must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for i in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print(" ")
