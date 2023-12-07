# https://school.programmers.co.kr/learn/courses/30/lessons/181855

def solution(strArr):
    check_list = [0] * 31
    
    for i in strArr:
        check_list[len(i)] += 1
        
    return max(check_list)