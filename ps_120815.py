# https://school.programmers.co.kr/learn/courses/30/lessons/120815

def solution(n):
    if n % 6 == 0:
        return n // 6
    elif n % 3 == 0:
        return n // 3
    elif n % 2 == 0:
        return n // 2
    else:
        return n