# https://school.programmers.co.kr/learn/courses/30/lessons/120913

def solution(my_str, n):
    return [my_str[n * i: n * i + n] for i in range(len(my_str) // n + 1) if my_str[n * i: n * i + n] != ""]