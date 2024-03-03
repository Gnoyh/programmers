# https://school.programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    result = [0] * len(prices)
    
    min_p = [prices[-1], len(prices) - 1]
    
    for i in range(len(prices) - 2, -1, -1):
        if prices[i] <= min_p[0]:
            min_p = [prices[i], i]
            
            result[i] = len(prices) - 1 - i
        else:
            for j in range(i + 1, min_p[1] + 1):
                if prices[i] > prices[j]:
                    result[i] = j - i
                    
                    break
                    
    return result