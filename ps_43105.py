# https://school.programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):
    result_list = [[triangle[0][0]]]
    
    for i in range(1, len(triangle)):
        check_list = []
        
        for j in range(i + 1):
            if j == 0:
                check_list.append(result_list[i - 1][0] + triangle[i][0])
            elif j == i:
                check_list.append(result_list[i - 1][-1] + triangle[i][-1])
            else:
                check_list.append(max(result_list[i - 1][j - 1], result_list[i - 1][j]) + triangle[i][j])
                
        result_list.append(check_list)
        
    return max(result_list[-1])