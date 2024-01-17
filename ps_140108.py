# https://school.programmers.co.kr/learn/courses/30/lessons/140108

def solution(s):
    result = 0
    x = ""
    x_count = 0
    other_count = 0
    
    for i in s:
        if x_count == 0:
            x = i
            
            x_count += 1
        else:
            if i == x:
                x_count += 1
            else:
                other_count += 1
        
        if x_count == other_count:
            result += 1
            
            x_count = 0
            other_count = 0
    
    if x_count + other_count > 0:
        result += 1
        
    return result