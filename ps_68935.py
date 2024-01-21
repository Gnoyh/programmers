# https://school.programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    result_str = ""
    
    while n > 0:
        result_str += str(n % 3)
        
        n //= 3
    
    return int(result_str, 3)