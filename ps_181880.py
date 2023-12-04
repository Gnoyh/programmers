# https://school.programmers.co.kr/learn/courses/30/lessons/181880

def solution(num_list):
    sum_int = 0
    
    for i in num_list:
        while i > 1:
            sum_int += 1
                
            if i % 2 == 0:
                i //= 2
            else:
                i = (i - 1) // 2
                
    return sum_int