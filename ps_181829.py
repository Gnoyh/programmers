# https://school.programmers.co.kr/learn/courses/30/lessons/181829

def solution(board, k):
    result = 0

    for i in range(k + 1):
        if i == len(board):
            break

        for j in range(0, k - i + 1):
            if j == len(board[0]):
                break

            result += board[i][j]

    return result