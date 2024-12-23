# https://school.programmers.co.kr/learn/courses/30/lessons/340198

def solution(mats, park):
    mats.sort(reverse = True)
    
    park_idx = []
    
    for i in range(len(park)):
        idx_list = []
        
        for j, v in enumerate(park[i]):
            if v == "-1":
                idx_list.append(j)
                
        park_idx.append(idx_list)
        
    for i in mats:
        for j in range(len(park_idx)):
            for k in park_idx[j]:
                result = i
                
                if j + i > len(park_idx):
                        result = -1
                        
                        break
                        
                for l in range(j, j + i):
                    for m in range(k, k + i):
                        if m not in park_idx[l]:
                            result = -1
                            
                            break
                            
                    if result == -1:
                        break
                
                if result != -1:
                    return result
                
    return -1