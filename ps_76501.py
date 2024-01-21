# https://school.programmers.co.kr/learn/courses/30/lessons/76501

def solution(absolutes, signs):
    result = 0
    
    for i, v in enumerate(absolutes):
        if signs[i]:
            result += v
        else:
            result -= v
            
    return result