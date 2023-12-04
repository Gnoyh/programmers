# https://school.programmers.co.kr/learn/courses/30/lessons/181884

def solution(numbers, n):
    sum_int = 0
    
    for i in numbers:
        sum_int += i
        
        if sum_int > n:
            return sum_int