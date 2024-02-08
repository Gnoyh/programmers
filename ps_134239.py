# https://school.programmers.co.kr/learn/courses/30/lessons/134239

def solution(k, ranges):
    result = []
    
    hail_list = [k]
    di_list = []
    
    while k > 1:
        if k % 2 == 0:
            k //= 2
        else:
            k = k * 3 + 1
            
        hail_list.append(k)
            
    for i in range(1, len(hail_list)):
        di_list.append(float(min(hail_list[i - 1], hail_list[i]) + abs(hail_list[i - 1] - hail_list[i]) / 2))
        
    for i in ranges:
        if i == [0, 0]:
            result.append(sum(di_list))
        elif i[0] <= len(di_list) + i[1]:
            result.append(sum(di_list[i[0]: len(di_list) + i[1]]))
        else:
            result.append(-1.0)
            
    return result