# https://school.programmers.co.kr/learn/courses/30/lessons/77884

def solution(left, right):
    return sum([i * (-1) if (i ** 0.5) % 1 == 0 else i for i in range(left, right + 1)])