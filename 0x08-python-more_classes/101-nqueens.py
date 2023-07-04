#!/usr/bin/python3
"""Solves the N-queens puzzle"""

import sys


def is_safe(board, row, col, N):
    """Check if the current position is safe for the queen."""

    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check the upper diagonal on the left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check the lower diagonal on the left side
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 'Q':
            return False
        i += 1
        j -= 1

    return True


def solve_nqueens(board, col, N):
    """Recursively solve the N queens problem."""

    # Base case: all queens are placed
    if col == N:
        print_solution(board, N)
        return

    # Try placing a queen in each row of the current column
    for row in range(N):
        if is_safe(board, row, col, N):
            # Place the queen
            board[row][col] = 'Q'

            # Recursively solve for the next column
            solve_nqueens(board, col + 1, N)

            # Backtrack: remove the queen from the current position
            board[row][col] = '.'


def print_solution(board, N):
    """Print the board configuration."""

    # Print the board configuration
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=' ')
        print()
    print()


def nqueens(N):
    """Solve the N queens problem and print all solutions."""

    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Create an empty chessboard
    board = [['.' for _ in range(N)] for _ in range(N)]

    # Solve the N queens problem
    solve_nqueens(board, 0, N)


# Check the number of arguments
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

# Get the value of N from the command line argument
try:
    N = int(sys.argv[1])
    nqueens(N)
except ValueError:
    print("N must be a number")
    sys.exit(1)
