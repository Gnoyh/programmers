# https://school.programmers.co.kr/learn/courses/30/lessons/120825

def solution(my_string, n):
    check_set = list(set(list(my_string)))
    
    for i in check_set:
        my_string = my_string.replace(i, i * n)
        
    return my_string