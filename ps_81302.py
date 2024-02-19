# https://school.programmers.co.kr/learn/courses/30/lessons/81302

def solution(places):
    result = []

    move_list = []

    for i in range(-2, 3):
        for j in range(-2, 3):
            if 0 < abs(i) + abs(j) <= 2:
                move_list.append([i, j])

    for i in places:
        check = 1

        for j in range(5):
            for k in range(5):
                if i[j][k] == "P":
                    for l in move_list:
                        if 0 <= j + l[0] < 5 and 0 <= k + l[1] < 5 and i[j + l[0]][k + l[1]] == "P":
                            if abs(l[0]) + abs(l[1]) == 1:
                                check = 0

                                break
                            else:
                                if abs(l[0]) == 2:
                                    if i[j + (l[0] // 2)][k] == "O":
                                        check = 0

                                        break
                                elif abs(l[1]) == 2:
                                    if i[j][k + (l[1] // 2)] == "O":
                                        check = 0

                                        break
                                else:
                                    if i[j + l[0]][k] == "O" or i[j][k + l[1]] == "O":
                                        check = 0

                                        break

                if check == 0:
                    break

            if check == 0:
                break

        result.append(check)

    return result