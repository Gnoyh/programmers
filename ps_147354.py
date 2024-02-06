# https://school.programmers.co.kr/learn/courses/30/lessons/147354

def solution(data, col, row_begin, row_end):
    result_list = []
    
    data.sort(key = lambda x: (x[col - 1], -x[0]))
    
    for i in range(row_begin - 1, row_end):
        result_list.append(sum([j % (i + 1) for j in data[i]]))
        
    for i in range(1, len(result_list)):
        result_list[i] ^= result_list[i - 1]
        
    return result_list[-1]