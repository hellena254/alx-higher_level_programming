#!/usr/bin/python3
"""Pascal triangle function."""


def pascal_triangle(n):
    """Returns a list of lists of integers representing
       the Pascal's triangle of n.
    Args:
       n (int): The size of triangle.
    Returns:
       A list of integer representingg the triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        i = triangle[-1]
        temp = [1]
        for j in range(len(i) - 1):
            temp.append(i[j] + i[j+ 1])
        temp.append(1)
        triangle.append(temp)

    return triangle
