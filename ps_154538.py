# https://school.programmers.co.kr/learn/courses/30/lessons/154538

def solution(x, y, n):
    result_idx = 0
    
    result_list = [[x, 0]]
    result_set = {x}
    
    while result_idx < len(result_list):
        check_x, result = result_list[result_idx][0], result_list[result_idx][1]
        
        if check_x == y:
            return result
        
        if check_x * 3 <= y and not check_x * 3 in result_set:
            result_list.append([check_x * 3, result + 1])
            result_set.add(check_x * 3)
            
        if check_x * 2 <= y and not check_x * 2 in result_set:
            result_list.append([check_x * 2, result + 1])
            result_set.add(check_x * 2)
            
        if check_x + n <= y and not check_x + n in result_set:
            result_list.append([check_x + n, result + 1])
            result_set.add(check_x + n)
            
        result_idx += 1
        
    return -1