# https://school.programmers.co.kr/learn/courses/30/lessons/147355

def solution(t, p):
    result = 0
    
    for i in range(0, len(t) - len(p) + 1):
        if int(t[i: i + len(p)]) <= int(p):
            result += 1
            
    return result