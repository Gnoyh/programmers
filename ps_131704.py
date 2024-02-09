# https://school.programmers.co.kr/learn/courses/30/lessons/131704

def solution(order):
    idx = 0
    
    sub_list = []
    
    for i in range(1, len(order) + 1):
        sub_list.append(i)
        
        while sub_list[-1] == order[idx]:
            idx += 1
            
            sub_list.pop()
            
            if not sub_list:
                break
        
    return idx