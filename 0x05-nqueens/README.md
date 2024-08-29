# 0x05 N-Queens
The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Write a program that solves the N queens problem.

Usage: nqueens N
    If the user called the program with the wrong number of arguments, print Usage: nqueens N, followed by a new line, and exit with the status 1
where N must be an integer greater or equal to 4
    If N is not an integer, print N must be a number, followed by a new line, and exit with the status 1
    If N is smaller than 4, print N must be at least 4, followed by a new line, and exit with the status 1
The program should print every possible solution to the problem
    One solution per line
    Format: see example
    You don’t have to print the solutions in a specific order
You are only allowed to import the sys module

## Function is_safe(board, row, col)

    Input: The current board, row, and col where you want to place a queen.

    Output: True if it's safe to place a queen at board[row][col], otherwise False.

    Check the column col on the upper side:
        For each row i from 0 to row-1:
            If board[i][col] == 1, return False.

    Check the upper left diagonal:
        Set i = row, j = col.
        While i >= 0 and j >= 0:
            If board[i][j] == 1, return False.
            Decrement i and j to move up the diagonal.

    Check the upper right diagonal:
        Set i = row, j = col.
        While i >= 0 and j < n:
            If board[i][j] == 1, return False.
            Decrement i and increment j to move up the diagonal.
    If no threats are found, return True.

## Recursive Function solve_nqueens(board, row, solutions)
    Input: The current board, the current row, and the list solutions to store all valid solutions.

    Output: None, but solutions will be updated with all valid queen placements.

    Set n as the size of the board.

    Base Case: If row == n (all queens are placed):
        Initialize an empty list solution.
        For each i from 0 to n-1:
            For each j from 0 to n-1:
                If board[i][j] == 1 (a queen is placed at this position):
                    Append the tuple [i, j] to solution.
        Append solution to solutions.
        Return.

    For each col from 0 to n-1:
        If is_safe(board, row, col) returns True:
            Place the queen by setting board[row][col] = 1.
            Recur by calling solve_nqueens(board, row + 1, solutions) to place the next queen.
            Backtrack by removing the queen (set board[row][col] = 0).

## Execution Flow:
    Initialize the board as a 2D list of size N x N filled with 0.
    Initialize an empty list solutions to store all valid solutions.
    Call the function solve_nqueens(board, 0, solutions) to start solving from the first row.
    Print each solution in solutions.
