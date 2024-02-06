# https://school.programmers.co.kr/learn/courses/30/lessons/142085

import heapq

def solution(n, k, enemy):
    result = k
    
    enemy_heap = []
    
    if k > len(enemy):
        return len(enemy)

    for i in enemy[: k]:
        heapq.heappush(enemy_heap, i)

    for i in enemy[k:]:
        if i > enemy_heap[0]:
            n -= heapq.heappop(enemy_heap)

            heapq.heappush(enemy_heap, i)
        else:
            n -= i

        if n < 0:
            break
        else:
            result += 1

    return result