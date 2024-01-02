# https://school.programmers.co.kr/learn/courses/30/lessons/120848

def solution(n):
    result = 1
    check = 1
    
    while check <= n:
        result += 1
        
        check *= result
        
    return result - 1