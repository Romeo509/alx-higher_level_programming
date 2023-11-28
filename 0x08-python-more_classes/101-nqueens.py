#!/usr/bin/python3
"""
N-Queens Solver

This program finds and prints solutions to the N-Queens puzzle,
where N is an integer greater than or equal to 4.

Usage:
    $ ./nqueens.py N

Attributes:
    chessboard (list): Represents the N x N chessboard.
    solutions (list): Contains lists of queen positions for each solution.

Each solution is represented as a list of lists, where each inner list
contains the row and column coordinates of a queen on the chessboard.
"""

import sys


def initialize_chessboard(size):
    """Initialize an N x N chessboard with empty cells.

    Args:
        size (int): The size of the chessboard.
    Returns:
        list: An initialized chessboard.
    """
    board = [[' ' for _ in range(size)] for _ in range(size)]
    return board


def deep_copy_chessboard(board):
    """Create a deep copy of a chessboard.

    Args:
        board (list): The chessboard to be copied.
    Returns:
        list: A deep copy of the chessboard.
    """
    if isinstance(board, list):
        return list(map(deep_copy_chessboard, board))
    return board


def get_solution_coordinates(board):
    """Retrieve the coordinates of queens from a solved chessboard.

    Args:
        board (list): A solved chessboard.
    Returns:
        list: Coordinates of queens in the format [[r, c], [r, c], ...].
    """
    solution = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == "Q":
                solution.append([row, col])
                break
    return solution


def mark_attacked_positions(board, row, col):
    """Mark attacked positions on the chessboard.

    Args:
        board (list): The current chessboard.
        row (int): Row coordinate of the last placed queen.
        col (int): Column coordinate of the last placed queen.
    """
    for c in range(col + 1, len(board)):
        board[row][c] = "x"  # Mark forward spots
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"  # Mark backward spots
    for r in range(row + 1, len(board)):
        board[r][col] = "x"  # Mark spots below
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"  # Mark spots above
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"  # Mark diagonally down to the right
        c += 1
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]  # Mark diagonally up to the left
        c -= 1
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"  # Mark diagonally up to the right
        c += 1
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"  # Mark diagonally down to the left
        c -= 1


def recursive_solve(board, row, queens, solutions):
    """Recursively solve the N-Queens puzzle.

    Args:
        board (list): The current chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        solutions (list): A list of lists containing solutions.
    Returns:
        list: Updated list of solutions.
    """
    if queens == len(board):
        solutions.append(get_solution_coordinates(board))
        return solutions

    for col in range(len(board)):
        if board[row][col] == " ":
            tmp_board = deep_copy_chessboard(board)
            tmp_board[row][col] = "Q"
            mark_attacked_positions(tmp_board, row, col)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    chessboard = initialize_chessboard(int(sys.argv[1]))
    solutions = recursive_solve(chessboard, 0, 0, [])
    for sol in solutions:
        print(sol)
