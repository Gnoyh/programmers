# https://school.programmers.co.kr/learn/courses/30/lessons/120866

def solution(board):
    n = len(board)

    for i in range(n):
        board[i] = [0] + board[i] + [0]

    board = [[0] * (n + 2)] + board + [[0] * (n + 2)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if board[i][j] % 2 == 1:
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        board[k][l] += 2

    board = [i[1: -1].count(0) for i in board[1: -1]]

    return sum(board)