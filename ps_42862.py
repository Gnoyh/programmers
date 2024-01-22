# https://school.programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    for i in set(lost + reserve):
        if i in set(lost) and i in set(reserve):
            lost.remove(i)
            reserve.remove(i)

    lost_set = set(lost)
    
    reserve.sort()
    
    for i in reserve:
        if i - 1 in lost_set:
            lost_set.remove(i - 1)
        elif i + 1 in lost_set:
            lost_set.remove(i + 1)
            
    return n - len(lost_set)