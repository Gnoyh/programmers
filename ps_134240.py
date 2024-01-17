# https://school.programmers.co.kr/learn/courses/30/lessons/134240

def solution(food):
    left_list = ""
    right_list = ""
    
    for i in range(1, len(food)):
        left_list += str(i) * (food[i] // 2)
        right_list = str(i) * (food[i] // 2) + right_list
        
    return left_list + "0" + right_list