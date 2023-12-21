# https://school.programmers.co.kr/learn/courses/30/lessons/120887

def solution(i, j, k):
    result = 0
    
    for x in range(i, j + 1):
        result += str(x).count(str(k))
        
    return result