# https://school.programmers.co.kr/learn/courses/30/lessons/17684

def solution(msg):
    result = []
    alpha_dict = {}
    num = 27
    
    for i, v in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        alpha_dict[v] = i + 1
        
    start_idx = 0
    end_idx = 1
    
    while end_idx <= len(msg):
        if end_idx == len(msg):
            if msg[start_idx: end_idx] in alpha_dict:
                result.append(alpha_dict[msg[start_idx: end_idx]])
            else:
                result.append(alpha_dict[msg[start_idx: end_idx - 1]])
                result.append(alpha_dict[msg[end_idx - 1: end_idx]])
            
            end_idx += 1
        else:
            if msg[start_idx: end_idx] in alpha_dict:
                end_idx += 1
            else:
                result.append(alpha_dict[msg[start_idx: end_idx - 1]])
                
                alpha_dict[msg[start_idx: end_idx]] = num
                num += 1
                start_idx = end_idx - 1
                
    return result