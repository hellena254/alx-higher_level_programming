#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for sub in matrix:
        for i in range(len(sub)):
            print("{:d}".format(sub[i]), end="")
            if i is not len(sub) - 1:
                print(" ", end="")
        print("")
