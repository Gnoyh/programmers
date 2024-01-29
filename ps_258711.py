# https://school.programmers.co.kr/learn/courses/30/lessons/258711

def solution(edges):
    result = [0] * 4
    
    max_num = max(map(max, edges)) + 1
    count_line = 0
    
    input_list = [0] * max_num
    output_list = [0] * max_num
    
    for i in edges:
        input_list[i[1]] += 1
        output_list[i[0]] += 1
            
    for i in range(1, max_num):
        if input_list[i] == 0 and output_list[i] >= 2:
            result[0] = i
            count_line = output_list[i]
        elif input_list[i] >= 2 and output_list[i] == 2:
            result[3] += 1
        elif output_list[i] == 0:
            result[2] += 1
            
    result[1] = count_line - (result[2] + result[3])
    
    return result