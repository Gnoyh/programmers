# https://school.programmers.co.kr/learn/courses/30/lessons/12938

def solution(n, s):
    if n > s:
        return [-1]
    else:
        min_num = s // n
        max_count = s % n
        
        min_list = [min_num] * (n - max_count)
        max_list = [min_num + 1] * max_count
        
        return min_list + max_list