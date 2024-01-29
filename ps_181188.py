# https://school.programmers.co.kr/learn/courses/30/lessons/181188

def solution(targets):
    result = 1
    
    targets.sort(key = lambda x: (x[1], x[0]))
    
    last_point = targets[0][1]
    
    for i in targets[1: ]:
        if i[0] >= last_point:
            result += 1
            
            last_point = i[1]
    
    return result