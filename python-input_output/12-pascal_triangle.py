#!/usr/bin/python3
"""Module providing pascal_triangle."""


def pascal_triangle(n):
    """Return Pascal's triangle of n as a list of lists."""
    if n <= 0:
        return []
    triangle = [[1]]
    for _ in range(1, n):
        previous = triangle[-1]
        row = [1]
        for i in range(len(previous) - 1):
            row.append(previous[i] + previous[i + 1])
        row.append(1)
        triangle.append(row)
    return triangle
