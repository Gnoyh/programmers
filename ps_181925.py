# https://school.programmers.co.kr/learn/courses/30/lessons/181925

def solution(numLog):
    check_dict = {1: "w", -1: "s", 10: "d", -10: "a"}

    result = ""

    for i in range(1, len(numLog)):
        result += check_dict[(numLog[i] - numLog[i - 1])]

    return result