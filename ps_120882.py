# https://school.programmers.co.kr/learn/courses/30/lessons/120882

def solution(score):
    check_list1 = [i[0] + i[1] for i in score]
    check_list2 = sorted(check_list1)[: : -1]
    
    return [check_list2.index(i) + 1 for i in check_list1]