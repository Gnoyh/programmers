# https://school.programmers.co.kr/learn/courses/30/lessons/68645

def solution(n):
    count = (n * (n + 1)) // 2
    
    all_list = [1] + [0] * (count - 1)
    cir_list = ["d", "r", "u", "l"]
    
    idx = 1
    num = 1
    cir_idx = 0
    
    for i in range(1, count):
        all_list[idx] = i + 1
            
        while i + 1 < count:
            if cir_list[cir_idx] == "d":
                if (idx + num + 1) < count and all_list[idx + num + 1] == 0:
                    idx = idx + num + 1
                    num += 1
                    
                    break
            elif cir_list[cir_idx] == "r":
                if (idx + 1) < count and all_list[idx + 1] == 0:
                    idx = idx + 1
                    
                    break
            elif cir_list[cir_idx] == "u":
                if (idx - num - 1) > 0 and all_list[idx - num - 1] == 0:
                    idx = idx - num - 1
                    num -= 1
                    
                    break
            else:
                if (idx - 1) > 0 and all_list[idx - 1] == 0:
                    idx = idx - 1
                    
                    break
                
            cir_idx = (cir_idx + 1) % 4
            
    return all_list