# https://school.programmers.co.kr/learn/courses/30/lessons/118667

def solution(queue1, queue2):
    result = 0
    
    start = 0
    end = len(queue1) - 1
    sum_q = sum(queue1)
    
    if (sum(queue1) + sum(queue2)) % 2 != 0:
        return -1
    
    check_sum = (sum(queue1) + sum(queue2)) // 2
    
    queue1 += queue2 + queue1
    
    while start <= end and end < len(queue1):
        if sum_q < check_sum and end != len(queue1) - 1:
            end += 1
            sum_q += queue1[end]
        elif sum_q > check_sum:
            sum_q -= queue1[start]
            start += 1
        elif sum_q == check_sum:
            return result
        else:
            break
        
        result += 1
    
    return -1