# https://school.programmers.co.kr/learn/courses/30/lessons/181921

def solution(l, r):
    check_list = [0, 5]
    result_list = []

    for i in range(1, len(str(r))):
        sub_list = []

        for j in check_list:
            sub_list.append(5 * (10 ** i) + j)

        check_list += sub_list

    for i in check_list:
        if i < l or i > r:
            continue

        result_list.append(i)