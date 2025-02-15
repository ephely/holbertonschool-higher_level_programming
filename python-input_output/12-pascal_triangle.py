#!/usr/bin/python3
""" 
Returns a list of lists of integers 
representing the Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """Represent a Pascal's Triangle of size n."""
    if n <= 0:
        return ([])
    triangle = []
    for i in range(n):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            for j in range(len(last_row) - 1):
                row.append(last_row[j] + last_row[j + 1])
            row.append(1)
        triangle.append(row)
    return (triangle)
