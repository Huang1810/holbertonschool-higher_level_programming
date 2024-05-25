#!/usr/bin/python3
"""
This module contains a function that\
 prints a square with the charactere #.
"""


def print_square(size):
    """
    prints square with the character #.

    args:
        aize (int): the lenght of the square.

    raises:
        TypeError: If the size is not an integer \
    or if the size is a float anf is less than 0.
        ValueError: If the size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)


if __name__ == "__main__":
    import doctest

    doctest.testfile("tests/4-print_square.txt")
