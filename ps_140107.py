# https://school.programmers.co.kr/learn/courses/30/lessons/140107

def solution(k, d):
    result = 0
    
    x = 0
    
    while x <= d:
        result += int(((d ** 2) - (x ** 2)) ** 0.5) // k + 1
        
        x += k
        
    return result