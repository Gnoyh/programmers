def solution(n):
    check_list = [[-1] * (n + 2)] + [[-1] + [0] * n + [-1] for _ in range(n)] + [[-1] * (n + 2)]
    mode = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    x, y, m = 1, 1, 0

    check_list[y][x] = 1

    for i in range(2, n ** 2 + 1):
        if check_list[y + mode[m][0]][x + mode[m][1]] != 0:
            m = (m + 1) % 4

        x += mode[m][1]
        y += mode[m][0]
        check_list[y][x] = i

    result = [i[1: -1] for i in check_list[1: -1]]

    return result