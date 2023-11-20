# https://school.programmers.co.kr/learn/courses/30/lessons/181926

def solution(n, control):
    for i in control:
        if i == "w":
            n += 1
        elif i == "s":
            n -= 1
        elif i == "d":
            n += 10
        else:
            n -= 10

    return n