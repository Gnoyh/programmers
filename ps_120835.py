# https://school.programmers.co.kr/learn/courses/30/lessons/120835

def solution(emergency):
    check_list = sorted(emergency)[: : -1]
    
    return [check_list.index(i) + 1 for i in emergency]