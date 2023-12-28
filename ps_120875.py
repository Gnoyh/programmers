# https://school.programmers.co.kr/learn/courses/30/lessons/120875

def solution(dots):
    if (dots[1][1] - dots[0][1]) / (dots[1][0] - dots[0][0]) == (dots[3][1] - dots[2][1]) / (dots[3][0] - dots[2][0]) or (dots[2][1] - dots[0][1]) / (dots[2][0] - dots[0][0]) == (dots[3][1] - dots[1][1]) / (dots[3][0] - dots[1][0]) or (dots[3][1] - dots[0][1]) / (dots[3][0] - dots[0][0]) == (dots[2][1] - dots[1][1]) / (dots[2][0] - dots[1][0]):
        return 1
    else:
        return 0