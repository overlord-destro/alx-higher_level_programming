#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        print("{:c}".format((ord(str[i]) - 32) 
if ord(str[i]) in range(97, 123) else ord(str[i])), end="")
    print(" ")
