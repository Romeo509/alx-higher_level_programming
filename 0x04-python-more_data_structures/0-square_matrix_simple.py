#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix using list comprehension with square values
    new_matrix = [[x**2 for x in row] for row in matrix]
    return new_matrix
