# https://school.programmers.co.kr/learn/courses/30/lessons/12928

def solution(n):
    result = 0
    
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            result += i
            
    return result + n