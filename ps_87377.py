# https://school.programmers.co.kr/learn/courses/30/lessons/87377

def solution(line):
    INF = float("inf")
    
    max_x = -INF
    min_x = INF
    max_y = -INF
    min_y = INF

    point_list = []

    for i in range(len(line) - 1):
        for j in range(i + 1, len(line)):
            A, B, E = line[i][0], line[i][1], line[i][2]
            C, D, F = line[j][0], line[j][1], line[j][2]

            if A * D - B * C == 0:
                continue
                
            x = (B * F - E * D) // (A * D - B * C)
            y = (E * C - A * F) // (A * D - B * C)

            if (B * F - E * D) % (A * D - B * C) == 0 and (E * C - A * F) % (A * D - B * C) == 0:
                point_list.append([x, y])

                max_x = max(max_x, x)
                min_x = min(min_x, x)
                max_y = max(max_y, y)
                min_y = min(min_y, y)

    result = [["." for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]

    for i in point_list:
        result[max_y - i[1]][i[0] - min_x] = "*"

    return ["".join(i) for i in result]