# https://school.programmers.co.kr/learn/courses/30/lessons/154540

def solution(maps):
    result = []

    move_list = [[-1, 0], [0, -1], [0, 1], [1, 0]]
    visited_list = [[0] * len(maps[0]) for _ in range(len(maps))]

    for i, v in enumerate(maps):
        for j, w in enumerate(v):
            if visited_list[i][j] == 0 and w != "X":
                check_sum = int(maps[i][j])
                check_idx = 0

                visited_list[i][j] = 1
                check_list = [[i, j]]

                while check_idx < len(check_list):
                    check_i = check_list[check_idx][0]
                    check_j = check_list[check_idx][1]

                    for k in move_list:
                        new_i = check_i + k[0]
                        new_j = check_j + k[1]

                        if 0 <= new_i < len(maps) and 0 <= new_j < len(maps[0]) and maps[new_i][new_j] != "X" and visited_list[new_i][new_j] == 0:
                            visited_list[new_i][new_j] = 1
                            
                            check_sum += int(maps[new_i][new_j])
                            
                            check_list.append([new_i, new_j])

                    check_idx += 1

                result.append(check_sum)

    if len(result) == 0:
        return [-1]
    else:
        return sorted(result)