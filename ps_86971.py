# https://school.programmers.co.kr/learn/courses/30/lessons/86971

def solution(n, wires):
    result = n

    top_list = [[] for _ in range(n + 1)]
    wires_list = [[0] * (n + 1) for _ in range(n + 1)]

    wires.sort(key = lambda x: (x[0], x[1]))

    for i in wires:
        top_list[i[0]].append(i[1])
        top_list[i[1]].append(i[0])

    for i in range(1, n + 1):
        if len(top_list[i]) == 1:
            wires_list[i][top_list[i][0]] = n - 1
        else:
            for j in top_list[i][: -1]:
                if i > j:
                    wires_list[i][j] = n - wires_list[j][i]
                elif len(top_list[j]) == 1:
                    wires_list[i][j] = 1
                else:
                    check_idx = 0
                    check_list = [j]

                    while check_idx < len(check_list):
                        check_set = set(check_list)
                        
                        for k in top_list[check_list[check_idx]]:
                            if k != i and k not in check_set:
                                check_list.append(k)
                            
                        check_idx += 1

                    wires_list[i][j] = check_idx

            wires_list[i][top_list[i][-1]] = n - 1 - sum(wires_list[i])

    for i in wires:
        result = min(result, abs(wires_list[i[0]][i[1]] * 2 - n))

    return result