# https://school.programmers.co.kr/learn/courses/30/lessons/120893

def solution(my_string):
    return "".join([i.upper() if i.islower() else i.lower() for i in my_string])