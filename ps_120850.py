# https://school.programmers.co.kr/learn/courses/30/lessons/120850

def solution(my_string):
    return sorted([int(i) for i in my_string if i.isdigit()])