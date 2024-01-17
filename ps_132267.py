# https://school.programmers.co.kr/learn/courses/30/lessons/132267

def solution(a, b, n):
    result = 0
    bottle = n
    
    while bottle >= a:
        result += (bottle // a) * b
        
        bottle = (bottle // a) * b + (bottle % a)
        
    return result