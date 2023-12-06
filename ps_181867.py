# https://school.programmers.co.kr/learn/courses/30/lessons/181867

def solution(myString):
    return [len(i) for i in list(myString.split("x"))]