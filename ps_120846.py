# https://school.programmers.co.kr/learn/courses/30/lessons/120846

def solution(n):
    check_list = [0] * (n + 1)
    
    for i in range(2, n // 2 + 1):
        if check_list[i] == 0:
            for j in range(i * 2, n + 1, i):
                check_list[j] = 1
                
    return sum(check_list)