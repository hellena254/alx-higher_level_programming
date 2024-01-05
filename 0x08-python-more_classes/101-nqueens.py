#!/usr/bin/python3
import sys
"""module sys"""


def is_safe(board, row, col, n):
    """
    Check if placing a queen at the given row and column is safe.

    Parameters:
        board (list): The current state of the chessboard.
        row (int): The current row being considered.
        col (int): The current column being considered.
        n (int): The size of the chessboard.

    Returns:
        bool: True if placing a queen is safe, False otherwise.
    """
    # Check if there is a queen in the same column or diagonals
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True

def solve_nqueens_util(board, row, n, solutions):
    """
    Recursively find all solutions to the N-Queens problem.

    Parameters:
        board (list): The current state of the chessboard.
        row (int): The current row being considered.
        n (int): The size of the chessboard.
        solutions (list): List to store the solutions.

    Returns:
        None
    """
    if row == n:
        solutions.append([[i, board[i]] for i in range(n)])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueens_util(board, row + 1, n, solutions)

def solve_nqueens(n):
    """
    Solve the N-Queens problem and print all solutions.

    Parameters:
        n (int): The size of the chessboard.

    Returns:
        None
    """
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solutions = []

    solve_nqueens_util(board, 0, n, solutions)

    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        solve_nqueens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
