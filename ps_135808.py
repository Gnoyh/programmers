# https://school.programmers.co.kr/learn/courses/30/lessons/135808

def solution(k, m, score):
    if len(score) < m:
        return 0
    
    result = 0
    
    score.sort(reverse = 1)
    
    for i in range(m - 1, len(score) - (len(score) % m), m):
        result += score[i] * m
        
    return result