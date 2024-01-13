# https://school.programmers.co.kr/learn/courses/30/lessons/172928

import copy

def solution(park, routes):
    direction_list = {"N": [-1, 0], "S": [1, 0], "W": [0, -1], "E": [0, 1]}

    dog_position = [0, 0]

    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                dog_position = [i, j]

                break

    width_position = len(park[0]) - 1
    height_position = len(park) - 1

    for i in routes:
        check = 1
        before_position = copy.deepcopy(dog_position)
        route = i.split()

        for j in range(int(route[1])):
            dog_position[0] += direction_list[route[0]][0]
            dog_position[1] += direction_list[route[0]][1]

            if dog_position[0] < 0 or dog_position[0] > height_position or dog_position[1] < 0 or dog_position[1] > width_position or park[dog_position[0]][dog_position[1]] == "X":
                check = 0

                break

        if check == 0:
            dog_position = before_position

    return [dog_position[0], dog_position[1]]