# https://school.programmers.co.kr/learn/courses/30/lessons/120840

def solution(balls, share):
    result = 1
    check = max(share, balls - share)
    
    for i in range(balls, check, -1):
        result *= i
        result //= (balls - i + 1)
        
    return result