# place n queens on n by n chest board in order for them not to be able to catch each other.

import numpy as np


def validate(bo, n):
    for row in range(0, n):
        if sum(bo[row,]) > 1:
            return False

    for col in range(0, n):
        if sum(bo[:, col]) > 1:
            return False

    diags = [bo[::-1, :].diagonal(i) for i in range(-n+1, n)]
    diags.extend(board.diagonal(i) for i in range(n - 1, -n, -1))

    for x in diags:
        if len(x) > 1:
            if sum(x) > 1:
                return False

    return True


def solve(board, row, n):
    if validate(board, n):
        if board.sum() == n:
            return True

    for col in range(0, n):
        board[row][col] = 1
        if validate(board, n):
            if solve(board, row + 1, n):
                return True
            board[row][col] = 0
        else:
            board[row, col] = 0
    return False


board = np.zeros((8, 8))

if solve(board, 0, 8):
    print(board)


