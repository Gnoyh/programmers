# https://school.programmers.co.kr/learn/courses/30/lessons/12914

from math import comb

def solution(n):
    result = 1
    check = 1
    n -= 1
    
    while n >= check:
        result += comb(n, check)
        
        n -= 1
        check += 1
    
    return result % 1234567