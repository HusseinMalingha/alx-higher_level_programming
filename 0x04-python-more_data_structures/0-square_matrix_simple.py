#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Returns a new matrix of same size and each value a square of each element
    """
    new_matrix = [[x**2 for x in row] for row in matrix]

    return new_matrix


if __name__ == "__main__":
    square_matrix_simple(matrix)
