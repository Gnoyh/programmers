# https://school.programmers.co.kr/learn/courses/30/lessons/181939

def solution(a, b):
    answer = max(int(str(a) + str(b)), int(str(b) + str(a)))

    return answer