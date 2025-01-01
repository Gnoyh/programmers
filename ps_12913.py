# https://school.programmers.co.kr/learn/courses/30/lessons/12913

def secmax(l):
    nl = sorted(l)
    
    return nl[-2]

def solution(land):
    for i, v in enumerate(land):
        if i > 0:
            for j in range(4):
                if land[i - 1][j] == max_num:
                    land[i][j] += secmax_num
                else:
                    land[i][j] += max_num
                    
        max_num = max(v)
        secmax_num = secmax(v)
                    
    return max(land[-1])