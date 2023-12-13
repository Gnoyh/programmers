# https://school.programmers.co.kr/learn/courses/30/lessons/120896

def solution(s):
    check_list = list(set([i for i in s]))
    result = []
    
    for i in check_list:
        if s.count(i) == 1:
            result.append(i)
            
    return "".join(sorted(result))