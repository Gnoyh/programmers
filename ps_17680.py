# https://school.programmers.co.kr/learn/courses/30/lessons/17680

def solution(cacheSize, cities):
    result = 0
    cache_list = []
    
    for i in cities:
        i = i.lower()
        
        if i in set(cache_list):
            result += 1
            
            cache_list.remove(i)
            cache_list.append(i)
        else:
            result += 5
            
            cache_list.append(i)
            
        if len(cache_list) > cacheSize:
            cache_list = cache_list[1: ]
        
    return result