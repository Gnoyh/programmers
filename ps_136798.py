# https://school.programmers.co.kr/learn/courses/30/lessons/136798

def solution(number, limit, power):
    divisor_list = [1] * (number + 1)
    
    for i in range(2, len(divisor_list)):
        for j in range(i, len(divisor_list), i):
            divisor_list[j] += 1
            
    result_list = [i if i <= limit else power for i in divisor_list[1: ]]
    
    return sum(result_list)