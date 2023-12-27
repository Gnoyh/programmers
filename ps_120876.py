# https://school.programmers.co.kr/learn/courses/30/lessons/120876

def solution(lines):
    check_list = []
    
    for i in range(3):
        check_set = [j for j in range(lines[i][0], lines[i][1])]
        
        check_list.append(set(check_set))
        
    return len((check_list[0] & check_list[1]) | (check_list[0] & check_list[2]) | (check_list[1] & check_list[2]))