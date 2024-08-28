#!/usr/bin/python3
"""
NQUEENS
the puzzle is a challenge of placing N non-attacking queens on an NXN board
"""
import sys

# check number of passed arguments
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

# value of passed argument
# if it is not a number or less than 4 exit status 1
N = sys.argv[1]

try:
    N = int(N)
    if not isinstance(N, int):
        print("N must be a number")
        exit(1)
    elif N < 4:
        print("N must be at least 4")
        exit(1)
except ValueError:
    print("N must be a number")
    exit(1)
except Exception as e:
    print(f"Error occurred {e}")
    exit(1)
