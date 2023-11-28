def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given number.

    Args:
        matrix (list of lists): Matrix of integers or floats.
        div (int or float): Divisor.

    Returns:
        list of lists: New matrix with elements rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   or if div is not a number.
        TypeError: If each row of the matrix doesn't have the same size.
        ZeroDivisionError: If div is equal to 0.
    """
    # Validate input types
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(element, (int, float)) for row in matrix for element in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Validate matrix dimensions
    if any(len(row) != len(matrix[0]) for row in matrix[1:]):
        raise TypeError("Each row of the matrix must have the same size")

    # Validate division by zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform matrix division and round to 2 decimal places
    result_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return result_matrix

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

result = matrix_divided(matrix, 3)
print(result)

