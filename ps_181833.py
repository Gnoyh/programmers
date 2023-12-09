# https://school.programmers.co.kr/learn/courses/30/lessons/181833

def solution(n):
    result = [[0] * n for _ in range(n)]
    
    for i in range(n):
        result[i][i] = 1
        
    return result