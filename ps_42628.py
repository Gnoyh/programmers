# https://school.programmers.co.kr/learn/courses/30/lessons/42628

def solution(operations):
    check_list = []
    
    for i in operations:
        if i == "D 1":
            if check_list:
                check_list.sort()
                
                check_list.pop()
        elif i == "D -1":
            if check_list:
                check_list.sort(reverse = True)
                
                check_list.pop()
        else:
            check_list.append(int(i[2: ]))
            
    if check_list:
        return [max(check_list), min(check_list)]
    else:
        return [0, 0]