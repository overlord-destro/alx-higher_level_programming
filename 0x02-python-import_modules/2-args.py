#!/usr/bin/python3
from sys import argv
if len(argv) - 1 == 0:
    print("{:d} arguments.".format(len(argv) - 1))
elif len(argv) - 1 == 1:
    print("{:d} argument:".format(len(argv) - 1))
else:
    print("{:d} arguments:".format(len(argv) - 1))
for i in range(1, len(argv)):
    print("{:d}: {:s}".format(i, argv[i]))
