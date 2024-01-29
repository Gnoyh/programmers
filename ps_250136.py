# https://school.programmers.co.kr/learn/courses/30/lessons/250136

def solution(land):
    result_list = [0] * len(land[0])

    move_list = [[-1, 0], [0, -1], [0, 1], [1, 0]]
    visited_list = [[0] * len(land[0]) for i in range(len(land))]

    for i, v in enumerate(land):
        for j, w in enumerate(v):
            if visited_list[i][j] == 0 and w != 0:
                visited_list[i][j] = 1
                location = 0

                oil_list = [[j, i]]

                while True:
                    if location == len(oil_list):
                        break

                    for x, y in move_list:
                        move_x = oil_list[location][0] + x
                        move_y = oil_list[location][1] + y

                        if move_x < 0 or move_x >= len(land[0]) or move_y < 0 or move_y >= len(land):
                            continue
                        elif visited_list[move_y][move_x] == 0 and land[move_y][move_x] != 0:
                            visited_list[move_y][move_x] = 1

                            oil_list.append([move_x, move_y])

                    location += 1

                for k in range(min(oil_list)[0], max(oil_list)[0] + 1):
                    result_list[k] += len(oil_list)

    return max(result_list)