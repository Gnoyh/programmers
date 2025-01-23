# https://school.programmers.co.kr/learn/courses/30/lessons/12979

def solution(n, stations, w):
    result = 0
    
    stations.append((-1) * w)
    stations.append(n + w + 1)
    
    stations.sort()
    
    for i in range(1, len(stations)):
        start = stations[i - 1] + w + 1
        end = stations[i] - w - 1
        
        if start <= end:
            result += (end - start) // (2 * w + 1) + 1
        
    return result