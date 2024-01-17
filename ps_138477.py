# https://school.programmers.co.kr/learn/courses/30/lessons/138477

def solution(k, score):
    result = []
    honor_list = []
    
    for i in score:
        if len(honor_list) < k:
            honor_list.append(i)
            
            result.append(min(honor_list))
        else:
            honor_list[honor_list.index(min(honor_list))] = max(min(honor_list), i)
            
            result.append(min(honor_list))
            
    return result