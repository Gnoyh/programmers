# https://school.programmers.co.kr/learn/courses/30/lessons/181930

def solution(a, b, c):
    answer = a + b + c

    if a == b and a == c:
        answer *= (a ** 2 + b ** 2 + c ** 2) * (a ** 3 + b ** 3 + c ** 3)
    elif a != b and a != c and b != c:
        return answer
    else:
        answer *= (a ** 2 + b ** 2 + c ** 2)

    return answer