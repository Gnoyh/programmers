# https://school.programmers.co.kr/learn/courses/30/lessons/181872

def solution(myString, pat):
    return myString[: len(myString) - myString[: : -1].index(pat[: : -1])]