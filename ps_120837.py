# https://school.programmers.co.kr/learn/courses/30/lessons/120837

def solution(hp):
    result = hp // 5
    
    hp = hp % 5
    
    result += hp // 3
    
    hp = hp % 3
    
    return result + hp