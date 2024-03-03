# https://school.programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    result = 1
    
    clothes_dict = {}
    
    for i in clothes:
        clothes_dict[i[1]] = clothes_dict.get(i[1], 1) + 1
    
    for i in list(clothes_dict.values()):
        result *= i
        
    return result - 1