# https://school.programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    result = 0
    idx = 0
    
    p_list = sorted(priorities)
    check_list = [[i, v] for i, v in enumerate(priorities)]
    
    while p_list:
        if check_list[idx][1] == p_list[-1]:
            p_list.pop()
            result += 1
            
            if check_list[idx][0] == location:
                return result
        else:
            check_list.append(check_list[idx])
            
        idx += 1