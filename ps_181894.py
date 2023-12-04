# https://school.programmers.co.kr/learn/courses/30/lessons/181894

def solution(arr):
    if 2 not in set(arr):
        return [-1]
    return arr[arr.index(2): len(arr) - arr[: : -1].index(2)]