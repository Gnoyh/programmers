# https://school.programmers.co.kr/learn/courses/30/lessons/120812

def solution(array):
    check_list = [0] * 1001
    
    for i in list(set(array)):
        check_list[i] = array.count(i)
        
    if check_list.count(max(check_list)) > 1:
        return -1
    else:
        return check_list.index(max(check_list))