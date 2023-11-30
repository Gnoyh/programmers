# https://school.programmers.co.kr/learn/courses/30/lessons/181900

def solution(my_string, indices):
    result_str = ""

    for i in range(len(my_string)):
        if i not in set(indices):
            result_str += my_string[i]

    return result_str