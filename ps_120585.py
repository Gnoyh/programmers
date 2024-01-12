# https://school.programmers.co.kr/learn/courses/30/lessons/120585

def solution(array, height):
    result = 0
    
    for i in array:
        if height < i:
            result += 1
            
    return result