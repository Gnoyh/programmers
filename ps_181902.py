# https://school.programmers.co.kr/learn/courses/30/lessons/181902

def solution(my_string):
    result_list = [0] * 52

    for i in my_string:
        if ord(i) <= 90:
            result_list[ord(i) - 65] += 1
        else:
            result_list[ord(i) - 71] += 1

    return result_list