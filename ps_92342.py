# https://school.programmers.co.kr/learn/courses/30/lessons/92342

def solution(n, info):
    result_list = []
    
    apeach_point = sum([10 - i for i in range(11) if info[i] > 0])
    
    sum_list = [[0, 0, [0] * 11]]
    ryan_list = []
    
    for i, v in enumerate(info):
        point_list = [v + 1]
        
        if v > 0:
            point_list.append((10 - i) * 2)
        else:
            point_list.append(10 - i)
            
        ryan_list.append(point_list)
        
    for i, v in enumerate(ryan_list):
        check_len = len(sum_list)
        
        for j in range(check_len):
            result_list = sum_list[j][2][: ]
            
            if v[0] + sum_list[j][0] <= n:
                result_list[i] += v[0]
                
                sum_list.append([v[0] + sum_list[j][0], v[1] + sum_list[j][1], result_list])
                
    sum_list.sort(key = lambda x: x[2][: : -1], reverse = True)
    sum_list.sort(key = lambda x: -x[1])
    
    if sum_list[0][1] <= apeach_point:
        return [-1]
    else:
        result_list = sum_list[0][2]
        
    if sum(result_list) < n:
        result_list[-1] += n - sum(result_list)
        
    return result_list