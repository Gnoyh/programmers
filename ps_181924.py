# https://school.programmers.co.kr/learn/courses/30/lessons/181924

def solution(arr, queries):
    for i in queries:
        arr[i[0]], arr[i[1]] = arr[i[1]], arr[i[0]]

    return arr