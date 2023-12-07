#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    m = list(map(list, zip(*my_list)))
    n = [x * y for x, y in zip(m[0], m[1])]
    return sum(n) / sum(m[1])
