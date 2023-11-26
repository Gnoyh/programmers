# https://school.programmers.co.kr/learn/courses/30/lessons/181909

def solution(my_string):
    result_list = []

    for i in range(len(my_string)):
        result_list.append(my_string[i: len(my_string)])

    result_list.sort()

    return result_list