# https://school.programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    result = 0

    new_board = [[]]

    for i in range(len(board)):
        new_line = []

        for j in board:
            if not j[i] == 0:
                new_line.insert(0, j[i])

        new_board.append(new_line)

    result_list = []

    for i in moves:
        if len(new_board[i]) > 0:
            doll = new_board[i].pop()

            if len(result_list) == 0:
                result_list.append(doll)
            else:
                if result_list[-1] == doll:
                    result += 2

                    result_list.pop()
                else:
                    result_list.append(doll)

    return result