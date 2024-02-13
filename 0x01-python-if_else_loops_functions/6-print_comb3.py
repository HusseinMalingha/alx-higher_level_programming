#!/usr/bin/python3
for i in range(0, 9):
    for j in range(1, 10):
        if (i,j) < (8,9):
            if i != j:
                print("{:d}{:d}, ".format(i, j), end="")
        else:
            print("{:d}{:d}".format(i, j))
