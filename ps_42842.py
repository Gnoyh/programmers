# https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    for i in range(3, int((brown + yellow) ** 0.5) + 1):
        if i * (brown // 2 - i + 2) == brown + yellow:
            return [brown // 2 - i + 2, i]