# https://school.programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    result = [0, 0]
    
    while s != "1":
        count = s.count("0")
        
        result[1] += count
        
        s = str(bin(len(s) - count))[2: ]
        
        result[0] += 1
    
    return result