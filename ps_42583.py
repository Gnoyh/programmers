# https://school.programmers.co.kr/learn/courses/30/lessons/42583

def solution(bridge_length, weight, truck_weights):
    result = 1
    
    truck_weights = truck_weights[: : -1]
    
    idx = 0
    sum_t = truck_weights.pop()
    
    b_list = [0] * (bridge_length - 1) + [sum_t]
    
    while truck_weights:
        if sum_t + truck_weights[-1] <= weight:
            sum_t += truck_weights[-1]
            b_list.append(truck_weights.pop())
            idx += 1
        else:
            b_list.append(0)
            idx += 1
            
        if b_list[idx] != 0:
            sum_t -= b_list[idx]
        
        result += 1
        
    return result + bridge_length