# https://school.programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    check_list = []
    
    for i in s:
        if not check_list:
            check_list.append(i)
        else:
            if check_list[-1] == i:
                check_list.pop()
            else:
                check_list.append(i)
                
    if check_list:
        return 0
    else:
        return 1