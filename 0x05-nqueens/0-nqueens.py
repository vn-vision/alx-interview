#!/usr/bin/python3
"""
NQUEENS
The puzzle is a challenge of placing N non-attacking queens on an N x N board
"""
import sys

# Check the number of passed arguments
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

# Value of passed argument
try:
    N = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4")
        exit(1)
except ValueError:
    print("N must be a number")
    exit(1)


# Function to check if a queen can be placed at board[row][col]
def is_safe(board, row, col):
    # Check this column on the upper side
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check the upper diagonal on the left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check the upper diagonal on the right side
    i, j = row, col
    while i >= 0 and j < len(board):
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


# Function to solve the N-Queens problem
def solve_nqueens(board, row, solutions):
    n = len(board)

    # If all queens are placed
    if row == n:
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for col in range(n):
        if is_safe(board, row, col):
            # Place queen
            board[row][col] = 1
            # Recur to place the rest of the queens
            solve_nqueens(board, row + 1, solutions)
            # Backtrack
            board[row][col] = 0


# Initialize board and list to store solutions
board = [[0] * N for _ in range(N)]
solutions = []

# Solve the problem
solve_nqueens(board, 0, solutions)

# Print all solutions
for solution in solutions:
    print(solution)
