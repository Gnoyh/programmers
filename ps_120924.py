# https://school.programmers.co.kr/learn/courses/30/lessons/120924

def solution(common):
    if (common[-1] - common[-2]) == (common[-2] - common[-3]):
        return common[-1] * 2 - common[-2]
    
    return common[-1] ** 2 // common[-2]    