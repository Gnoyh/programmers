# https://school.programmers.co.kr/learn/courses/30/lessons/120922

def solution(M, N):
    result = min(M, N) - 1 + min(M, N) * (max(M, N) - 1)
    
    return result