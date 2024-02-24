# https://school.programmers.co.kr/learn/courses/30/lessons/72411

def comb(arr, n):
    result = []
    
    if n == 1:
        for i in arr:
            result.append(i)
    else:
        for i in range(len(arr) - n + 1):
            for j in comb(arr[i + 1: ], n - 1):
                result.append(arr[i] + j)
                
    return result

def solution(orders, course):
    result = []
    
    orders_set = set()
    
    orders_dict = {}
    
    for i in course:
        orders_dict[i] = {}
    
    for i, v in enumerate(orders):
        orders[i] = "".join(sorted(v))
    
    for i in orders:
        for j in course:
            for k in comb(i, j):
                if k in orders_set:
                    orders_dict[j][k] += 1
                else:
                    orders_set.add(k)
                    
                    orders_dict[j][k] = 1
                    
    for i in course:
        max_int = 2
        
        max_list = []
        
        for k, v in orders_dict[i].items():
            if v > max_int:
                max_int = v
                
                max_list = [k]
            elif v == max_int:
                max_list.append(k)
                
        result += max_list
        
    return sorted(result)