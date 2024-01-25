# https://school.programmers.co.kr/learn/courses/30/lessons/12940

def solution(n, m):
    result = []
    
    for i in range(min(n, m), 0, -1):
        if m % i == 0 and n % i == 0:
            result.append(i)
            
            break
            
    result.append(n * m // result[0])
    
    return result