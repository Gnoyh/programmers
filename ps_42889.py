# https://school.programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    fail_dict = {}
    
    stages.sort()
    
    for i in range(1, N + 1):
        fail_dict[i] = 0
    
    for i in set(stages):
        if not i == N + 1:
            fail_dict[i] = stages.count(i) / (len(stages) - stages.index(i))
        
    return sorted(fail_dict, key = lambda x: fail_dict[x], reverse = True)