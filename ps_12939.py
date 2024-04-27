# https://school.programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    check = list(map(int, s.split(" ")))
    
    return str(min(check)) + " " + str(max(check))