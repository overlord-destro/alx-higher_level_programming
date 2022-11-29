#!/usr/bin/python3
for i in range(100):
    for j in range(100):
        if i >= 8 or j >= 10:
            break
        if i >= j:
            continue
        print("{:d}{:d}, ".format(i, j), end="")
print("89")
