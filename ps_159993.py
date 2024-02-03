# https://school.programmers.co.kr/learn/courses/30/lessons/159993

def solution(maps):
    result_idx = 0

    result_list = []
    move_list = [[-1, 0], [0, -1], [0, 1], [1, 0]]
    visited_list = [[0] * len(maps[0]) for _ in range(len(maps))]

    for i, v in enumerate(maps):
        if "S" in v:
            result_list.append([i, v.index("S"), 0])

    while result_idx < len(result_list):
        h, w, c = result_list[result_idx]

        if maps[h][w] == "L":
            result_idx = 0
            result_list = [[h, w, c]]

            break

        for i in move_list:
            check_h = h + i[0]
            check_w = w + i[1]

            if 0 <= check_h < len(maps) and 0 <= check_w < len(maps[0]) and maps[check_h][check_w] != "X" and visited_list[check_h][check_w] == 0:
                result_list.append([check_h, check_w, c + 1])

                visited_list[check_h][check_w] = 1

        result_idx += 1
        
    visited_list = [[0] * len(maps[0]) for _ in range(len(maps))]

    while result_idx < len(result_list):
        h, w, c = result_list[result_idx]

        if maps[h][w] == "E":
            return c

        for i in move_list:
            check_h = h + i[0]
            check_w = w + i[1]

            if 0 <= check_h < len(maps) and 0 <= check_w < len(maps[0]) and maps[check_h][check_w] != "X" and visited_list[check_h][check_w] == 0:
                result_list.append([check_h, check_w, c + 1])

                visited_list[check_h][check_w] = 1

        result_idx += 1

    return -1