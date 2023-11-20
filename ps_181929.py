# https://school.programmers.co.kr/learn/courses/30/lessons/181929

from math import prod


def solution(num_list):
    if prod(num_list) > sum(num_list) ** 2:
        return 0

    return 1