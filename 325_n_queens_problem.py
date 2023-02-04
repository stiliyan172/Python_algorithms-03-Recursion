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

# class Board(object):
#     def __init__(self, n):
#         self.n = n
#         self.board = [[0 for _ in range(n)] for _ in range(n)]
#
#     def solve(self, row, result, output):
#         if row == self.n:
#             output.append(result[:])
#             return
#
#         for col in range(self.n):
#             if self.isSafeCell(row, col):
#                 self.board[row][col] = 1
#                 result.append((row, col))
#                 self.solve(row + 1, result, output)
#                 self.board[row][col] = 0
#                 result.pop()
#
#     def nQueens(self):
#         result = []
#         output = []
#         self.solve(0, result, output)
#         return output
#
#     def isSafeCell(self, row, col):
#
#         # Vertical check
#         for r in range(row - 1, -1, -1):
#             if self.board[r][col]:
#                 return False
#
#         # Main diagonal check
#         r = row - 1
#         c = col - 1
#         while r >= 0 and c >= 0:
#             if self.board[r][c]:
#                 return False
#             r -= 1
#             c -= 1
#
#         # Minor diagonal check
#         r = row - 1
#         c = col + 1
#         while r >= 0 and c < self.n:
#             if self.board[r][c]:
#                 return False
#             r -= 1
#             c += 1
#
#         return True
#
#     def display(self):
#         for row in self.board:
#             print(row)
#
#
# b = Board(4)
# b.nQueens()