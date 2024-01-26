# https://school.programmers.co.kr/learn/courses/30/lessons/12921

def solution(n):
    num_list = [0] * (n + 1)
    
    for i in range(2, int(n ** (1 / 2)) + 1 + 1):
        if num_list[i] == 0:
            for j in range(i * 2, n + 1, i):
                num_list[j] = 1
                
    return num_list.count(0) - 2