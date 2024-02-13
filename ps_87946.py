# https://school.programmers.co.kr/learn/courses/30/lessons/87946

def solution(k, dungeons):
    result_list = [[k, 0]]
    
    dungeons.sort(key = lambda x: (x[1] - x[0], -x[0]))
    
    for i in dungeons:
        len_result = len(result_list)
        
        for j in range(len_result):
            if result_list[j][0] >= i[0]:
                result_list.append([result_list[j][0] - i[1], result_list[j][1] + 1])
                
    return sorted(result_list, key = lambda x: -x[1])[0][1]