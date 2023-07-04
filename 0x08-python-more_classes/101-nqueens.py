#!/usr/bin/python3
"""Solution to the N-queens puzzle"""


import sys


def is_safe(board, row, col, N):
    """
    Check if it is safe to place a queen at the given position on the board.
    """
    # Check if there is a queen in the current row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def nqueens(board, col, N):
    """
    Solve the N Queens problem using backtracking.
    """
    if col >= N:
        print([[i, j] for i, row in enumerate(board) for j, val in enumerate(row) if val])
        return

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            nqueens(board, col + 1, N)
            board[i][col] = 0


def main():
    """
    Main function that validates the input and solves the N Queens problem.
    """
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the board with all zeros
    board = [[0 for _ in range(N)] for _ in range(N)]

    # Solve the N Queens problem
    nqueens(board, 0, N)


if __name__ == "__main__":
    main()
