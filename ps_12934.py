# https://school.programmers.co.kr/learn/courses/30/lessons/12934

def solution(n):
    num = n ** (1 / 2)
    
    if num % 1 == 0:
        return (num + 1) ** 2
    else:
        return -1