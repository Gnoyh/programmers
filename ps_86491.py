# https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    min_size = 0
    max_size = 0
    
    for i in sizes:
        min_size = max(min_size, min(i))
        max_size = max(max_size, max(i))
        
    return min_size * max_size