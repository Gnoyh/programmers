# https://school.programmers.co.kr/learn/courses/30/lessons/181879

from math import prod

def solution(num_list):
    if len(num_list) > 10:
        return sum(num_list)
    
    return prod(num_list)