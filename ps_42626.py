# https://school.programmers.co.kr/learn/courses/30/lessons/42626

import heapq

def solution(scoville, K):
    result = 0
    
    s_heap = []
    
    for i in scoville:
        heapq.heappush(s_heap, i)
        
    while s_heap[0] < K:
        sum_s = 0
        
        if len(s_heap) < 2:
            return -1
        
        for i in range(1, 3):
            sum_s += heapq.heappop(s_heap) * i
            
        heapq.heappush(s_heap, sum_s)
        
        result += 1
        
    return result