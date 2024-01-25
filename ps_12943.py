# https://school.programmers.co.kr/learn/courses/30/lessons/12943

def solution(num):
    result = 0
    
    while num > 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
            
        result += 1
        
        if result == 500:
            result = -1
            
            break
            
    return result