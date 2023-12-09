# https://school.programmers.co.kr/learn/courses/30/lessons/181837

def solution(order):
    result = 0
    
    for i in order:
        if "cafelatte" in i:
            result += 5000
        else:
            result += 4500
            
    return result