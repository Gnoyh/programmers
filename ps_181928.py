# https://school.programmers.co.kr/learn/courses/30/lessons/181928

def solution(num_list):
    odd = ""
    even = ""

    for i in num_list:
        if i % 2 == 1:
            odd += str(i)
        else:
            even += str(i)

    return int(odd) + int(even)