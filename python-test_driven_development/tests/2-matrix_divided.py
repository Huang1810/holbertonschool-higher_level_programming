#!/usr/bin/python3
"""
This module provide a function `matrix_divided` \
    that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists of int/float): The matrix to be divided.
        div (int/float): The divisor.

    Returns:
        list of lists of float: New matrix with each element divided by div.

    Raises:
        TypeError: If matrix elements are not lists of integers/floats,
                   or if div is not a number.
        ZeroDivisionError: If div is zero.
        TypeError: If rows of the matrix are not of the same size.
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    row_lenght = len(matrix[0])
    for row in matrix:
        if len(row) != row_lenght:
            raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
            if num == float('inf') or num == float('-inf') or num != num:
                raise OverflowError("cannot convert \
float infinity or NaN to integer")
            new_row.append(round(num / div, 2))
        new_matrix.append(new_row)

    return new_matrix


if __name__ == "__main__":
    import doctest

    doctest.testfile("tests/2-matrix_divided.txt")
