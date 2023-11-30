#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    # get all names defined
    names = []
    for i in dir(hidden_4):
        if not i.startswith('__'):
            names.append(i)

    # sort the names in alphabets
    sort_names = sorted(names)

    # print each name on a new line
    for i in sort_names:
        print(i)
