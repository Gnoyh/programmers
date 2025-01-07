# https://school.programmers.co.kr/learn/courses/30/lessons/12927

def solution(n, works):
    works.sort(reverse = True)
    
    idx = 0
    result = 0
    
    if sum(works) <= n:
        return 0
    
    while n > 0 and idx < len(works):
        works[idx] -= 1
        n -= 1
        
        if idx == len(works) - 1:
            idx = 0
        else:
            if works[idx] == works[idx + 1]:
                idx = 0
            elif works[idx] < works[idx + 1]:
                idx += 1
            else:
                if works[0] >= works[idx]:
                    idx = 0
                    
    for i in works:
        result += i ** 2
        
    return result