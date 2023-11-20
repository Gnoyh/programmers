# https://school.programmers.co.kr/learn/courses/30/lessons/181930

def solution(a, b, c):
    check_list = [a, b, c]

    if len(set(check_list)) == 3:
        return a + b + c
    elif len(set(check_list)) == 2:
        return (a + b + c) * (a ** 2 + b ** 2 + c ** 2)
    else:
        return a * (a ** 2) * (a ** 3) * 27