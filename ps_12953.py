# https://school.programmers.co.kr/learn/courses/30/lessons/12953

import math

def solution(arr):
    result = 1
    
    for i in arr:
        result = (result * i) // math.gcd(result, i)
        
    return result