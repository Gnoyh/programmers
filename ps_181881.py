# https://school.programmers.co.kr/learn/courses/30/lessons/181881

def solution(arr):
    count_list = []
    
    for i in arr:
        count = 0
        
        while True:
            if i >= 50 and i % 2 == 0:
                count += 1
                i = i // 2
                
                continue
            elif i < 50 and i % 2 == 1:
                count += 1
                i = i * 2 + 1
                
                continue
                
            break
            
        count_list.append(count)
        
    return max(count_list)