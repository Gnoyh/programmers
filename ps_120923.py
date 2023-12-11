# https://school.programmers.co.kr/learn/courses/30/lessons/120923

def solution(num, total):
    if num % 2 == 0:
        check = ((total // (num // 2)) - num + 1) // 2
        
        return [i for i in range(check, check + num)]
    
    check = total // num
    
    return [i for i in range(check - (num // 2), check + (num // 2) + 1)]