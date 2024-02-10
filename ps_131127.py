# https://school.programmers.co.kr/learn/courses/30/lessons/131127

def solution(want, number, discount):
    result = 0
    
    want_set = {}
    result_set = {}
    
    for i in range(len(want)):
        want_set[want[i]] = number[i]
        result_set[want[i]] = 0
    
    for i in discount[: 10]:
        if result_set.get(i) != None:
            result_set[i] += 1
            
    if want_set == result_set:
        result += 1
        
    for i in range(10, len(discount)):
        if result_set.get(discount[i - 10]) != None:
            result_set[discount[i - 10]] -= 1
        
        if result_set.get(discount[i]) != None:
            result_set[discount[i]] += 1
            
        if want_set == result_set:
            result += 1
            
    return result