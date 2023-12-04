# https://school.programmers.co.kr/learn/courses/30/lessons/181878

def solution(myString, pat):
    return int(pat.upper() in myString.upper())