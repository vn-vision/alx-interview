#!/usr/bin/python3
"""
Rotate 2d Matrix 90 degrees

    First transpose the matrix in Single line
    Reverse the order of the the columns to achieve rotation
"""


def rotate_2d_matrix(matrix):
    """
    rotate n x n 2d matrix 90 degrees clockwise
    """

    # transpose the matrix in single line
    # the new matrix will have cols equal to old matrix rows and vice versa\
    # only when i < j, above the diagonal, for efficiency and avoid
    # swapping back to the original matrix
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix[i])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # reverse the rows to achieve 90 degree rotation clockwise
    for row in matrix:
        row.reverse()
