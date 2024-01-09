# https://school.programmers.co.kr/learn/courses/30/lessons/120834

def solution(age):
    check_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    
    return "".join([check_list[int(i)] for i in str(age)])