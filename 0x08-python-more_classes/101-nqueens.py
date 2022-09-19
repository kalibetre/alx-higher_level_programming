#!/usr/bin/python3
"""Module 101-nqueens

This Module contains a program to solve N queens puzzle
"""

import sys


def run_solver():
    """Solves N Queen Problem"""
    check_argv()

    n = int(sys.argv[1])
    board = [[None for _ in range(n)] for _ in range(n)]

    cols = set()
    diag_1 = set()
    diag_2 = set()

    def solve_board(row):
        if row == n:
            solution = []
            i = 0
            for row in board:
                solution.append([i, row.index("Q")])
                i += 1

            print(solution)
            return

        for col in range(n):
            if col in cols or (row + col) in diag_1 or (row - col) in diag_2:
                continue

            cols.add(col)
            diag_1.add(row + col)
            diag_2.add(row - col)
            board[row][col] = "Q"
            solve_board(row + 1)
            cols.remove(col)
            diag_1.remove(row + col)
            diag_2.remove(row - col)
            board[row][col] = None

    solve_board(0)


def check_argv():
    """Checks if the program argument is correct"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)

    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)


if __name__ == "__main__":
    run_solver()
