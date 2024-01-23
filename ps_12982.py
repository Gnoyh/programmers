# https://school.programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    check_max = 0
    
    d.sort(reverse = True)
    
    if budget >= sum(d):
        return len(d)
    
    for i in range(len(d)):
        check_max += d[i]
        
        if budget >= sum(d) - check_max:
            return len(d) - (i + 1)