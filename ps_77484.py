# https://school.programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    count = 0
    
    for i in lottos:
        if i in set(win_nums):
            count += 1
            
    return [min(7 - (count + lottos.count(0)), 6), min(7 - count, 6)]