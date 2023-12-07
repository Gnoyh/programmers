# https://school.programmers.co.kr/learn/courses/30/lessons/181857

def solution(arr):
    for i in range(11):
        if len(arr) <= 2 ** i:
            return arr + [0] * (2 ** i - len(arr))