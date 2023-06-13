#!/usr/bin/python3
"""Define pascal traingle """


def pascal_triangle(n):
    """defien pascal triangle function"""

    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    triangle = [[1]]
    for i in range(n - 1):
        triangle.append([i + k for i, k in zip(triangle[-1] + [0],
                                               [0] + triangel[-1])])
    return triangle
