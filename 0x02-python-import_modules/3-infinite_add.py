#!/usr/bin/python3
import sys
if __name__ == "__main__":
    num_args = sys.argv[1:]

    if not num_args:
        print("0")
    else:
        total = sum(int(i) for i in num_args)
        print(total)
