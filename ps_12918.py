# https://school.programmers.co.kr/learn/courses/30/lessons/12918

def solution(s):
    if len(s) == 4 or len(s) == 6:
        if s.isdigit():
            return True
    
    return False