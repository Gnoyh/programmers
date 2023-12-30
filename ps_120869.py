# https://school.programmers.co.kr/learn/courses/30/lessons/120869

def solution(spell, dic):
    for i in dic:
        check = 1
        
        for j in spell:
            if not i.count(j) == 1:
                check = 0
                
                break
        
        if check == 1:
            return 1
    
    return 2