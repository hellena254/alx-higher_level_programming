#!/usr/bin/python3
def magic_calculation(a, b):
    res = 0
    for i in range(1, 4):
        try:
            if i > a:
                raise Exception('Too far')
            res += (a ** b) / 1
        except Exception:
            res += b + a
            break

    return res
