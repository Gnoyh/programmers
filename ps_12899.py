# https://school.programmers.co.kr/learn/courses/30/lessons/12899

def solution(n):
    num_list = ['4', '1', '2']
    result = ""
    
    while n > 0:
        result = num_list[n % 3] + result
        
        if n % 3 == 0:
            n = (n // 3) - 1
        else:
            n //= 3
        
    if n != 0:
        result = num_list[n] + result
    
    return result