# https://school.programmers.co.kr/learn/courses/30/lessons/138476

def solution(k, tangerine):
    result = 0
    
    result_dict = {}
    
    for i in set(tangerine):
        result_dict[i] = 0
        
    for i in tangerine:
        result_dict[i] += 1
        
    result_dict = sorted(result_dict.items(), key = lambda x: x[1], reverse = True)
    
    for i in result_dict:
        result += 1
        k -= i[1]
        
        if k <= 0:
            return result