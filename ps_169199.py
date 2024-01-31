# https://school.programmers.co.kr/learn/courses/30/lessons/169199

def solution(board):
    result_idx = 0

    result_list = []
    slide_list = [[-1, 0], [0, -1], [0, 1], [1, 0]]
    visited_list = [[0] * len(board[0]) for _ in range(len(board))]

    for i in range(len(board)):
        if "R" in board[i]:
            result_list.append([i, board[i].index("R"), 0])

            visited_list[i][board[i].index("R")] = 1

    while result_idx < len(result_list):
        h, w, c = result_list[result_idx]

        if board[h][w] == "G":
            return c

        for i in slide_list:
            check_h = h
            check_w = w

            while 0 <= check_h + i[0] < len(board) and 0 <= check_w + i[1] < len(board[0]) and board[check_h + i[0]][check_w + i[1]] != "D":
                check_h += i[0]
                check_w += i[1]

            if visited_list[check_h][check_w] == 0:
                result_list.append([check_h, check_w, c + 1])
                
                visited_list[check_h][check_w] = 1

        result_idx += 1

    return -1