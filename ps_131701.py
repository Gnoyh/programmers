# https://school.programmers.co.kr/learn/courses/30/lessons/131701

def solution(elements):
    len_ele = len(elements)
    sum_set = {sum(elements)}
    
    elements += elements[: -2]
    
    for i in range(len_ele):
        check_sum = 0
        
        for j in range(len_ele - 1):
            check_sum += elements[i + j]
            
            sum_set.add(check_sum)
            
    return len(sum_set)