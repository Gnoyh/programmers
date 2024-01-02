# https://school.programmers.co.kr/learn/courses/30/lessons/120852

def solution(n):
    result = set()
    
    check = 2
    
    while n > 1:
        if n % check == 0:
            n = n // check
            
            result.add(check)
        else:
            check += 1
    
    return sorted(list(result))