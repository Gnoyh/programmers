# https://school.programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    check = bin(n)[2: ].count("1")
    
    n += 1
    
    while bin(n)[2: ].count("1") != check:
        n += 1
        
    return n