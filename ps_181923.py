# https://school.programmers.co.kr/learn/courses/30/lessons/181923

def solution(arr, queries):
    result = []

    for i in queries:
        int_min = 1000001

        for j in range(i[0], i[1] + 1):
            if arr[j] > i[2]:
                int_min = min(int_min, arr[j])

        if int_min == 1000001:
            result.append(-1)
        else:
            result.append(int_min)

    return result