# https://school.programmers.co.kr/learn/courses/30/lessons/120905

def solution(s1, s2):
    return len(s1) + len(s2) - len(set(s1 + s2))