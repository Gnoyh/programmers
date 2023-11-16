# https://school.programmers.co.kr/learn/courses/30/lessons/181938

def solution(a, b):
    answer = max(int(str(a) + str(b)), a * b * 2)

    return answer