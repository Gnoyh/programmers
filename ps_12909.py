# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    check = 0
    
    s_dict = {"(": 1, ")": -1}
    
    for i in s:
        check += s_dict[i]
        
        if check < 0:
            return False
        
    if check == 0:
        return True
    else:
        return False