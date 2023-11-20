# https://school.programmers.co.kr/learn/courses/30/lessons/181919

def solution(n):
    result_list = [n]

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1

        result_list.append(n)

    return result_list