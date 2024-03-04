# https://school.programmers.co.kr/learn/courses/30/lessons/42860

def solution(name):
    result = 0
    
    move = len(name) - 1
    
    for i, v in enumerate(name):   
        result += min(ord(v) - ord('A'), ord('Z') - ord(v) + 1)
        
        next_m = i + 1
        
        while next_m < len(name) and name[next_m] == 'A':
            next_m += 1
            
        move = min(move, 2 * i + len(name) - next_m, i + 2 * (len(name) - next_m))
        
    return result + move