# https://school.programmers.co.kr/learn/courses/30/lessons/161989

def solution(n, m, section):
    result = 0
    start_section = 0
    
    for i in section:
        if start_section < i:
            start_section = i + m - 1
            
            result += 1
            
    return result