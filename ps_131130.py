# https://school.programmers.co.kr/learn/courses/30/lessons/131130

def solution(cards):
    result_list = []
    cards_dict = {}
    
    for i in range(len(cards)):
        cards_dict[i + 1] = cards[i]
        
    for i in range(1, len(cards) + 1):
        before_idx = 0
        idx = i
        count = 0
        
        while cards_dict[idx] != 0:
            before_idx = idx
            idx = cards_dict[idx]
            cards_dict[before_idx] = 0
            
            count += 1
            
        result_list.append(count)
        
    result_list.sort()
    
    return result_list[-1] * result_list[-2]