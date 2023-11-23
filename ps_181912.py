# https://school.programmers.co.kr/learn/courses/30/lessons/181912

def solution(intStrs, k, s, l):
    result_list = []

    for i in intStrs:
        if int(i[s: s + l]) > k:
            result_list.append(int(i[s: s + l]))

    return result_list