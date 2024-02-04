# https://school.programmers.co.kr/learn/courses/30/lessons/152996

def solution(weights):
    result = 0

    result_list = [0] * 4001

    for i in weights:
        result_list[i] += 1
        
    for i in result_list:
        if i > 1:
            result += (i * (i - 1)) // 2

    result = -(result * 2)
    
    result_list = [0] * 4001

    for i in weights:
        for j in range(2, 5):
            result_list[i * j] += 1

    for i in result_list:
        if i > 1:
            result += (i * (i - 1)) // 2

    return result