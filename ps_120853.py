# https://school.programmers.co.kr/learn/courses/30/lessons/120853

def solution(s):
    result = 0
    check = 0
    
    s = s.split()
    
    for i in s:
        if i == "Z":
            result -= check
        else:
            check = int(i)
            result += check
            
    return result