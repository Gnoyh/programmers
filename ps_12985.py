# https://school.programmers.co.kr/learn/courses/30/lessons/12985

def solution(n,a,b):
    result = 0
    
    while a != b:
        result += 1
        
        a = (a + 1) // 2
        b = (b + 1) // 2
        
        if a == b:
            return result