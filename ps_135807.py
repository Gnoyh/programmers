# https://school.programmers.co.kr/learn/courses/30/lessons/135807

from math import gcd

def solution(arrayA, arrayB):
    gcd_a = arrayA[0]
    gcd_b = arrayB[0]
    
    for i in arrayA[1: ]:
        gcd_a = gcd(gcd_a, i)
        
    for i in arrayB[1: ]:
        gcd_b = gcd(gcd_b, i)
        
    result_list = [gcd_a, gcd_b]
    
    for i in arrayB:
        if i % gcd_a == 0:
            result_list[0] = 0
            
    for i in arrayA:
        if i % gcd_b == 0:
            result_list[1] = 0
            
    return max(result_list)