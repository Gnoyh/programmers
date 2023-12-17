# https://school.programmers.co.kr/learn/courses/30/lessons/120891

def solution(order):
    result = 0
    
    for i in ["3", "6", "9"]:
        result += str(order).count(i)
            
    return result