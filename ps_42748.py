# https://school.programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    result = []
    
    for i in commands:
        sorted_list = sorted(array[i[0] - 1: i[1]])
        
        result.append(sorted_list[i[2] - 1])
        
    return result