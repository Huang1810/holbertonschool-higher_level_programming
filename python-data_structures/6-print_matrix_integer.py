#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    elif matrix == [[]]:
        print()
    else:
        for row in matrix:
            for i, num in enumerate(row):
                if i == len(row) - 1:
                    print("{:d}".format(num))
                else:
                    print("{:d}".format(num), end=" ")
