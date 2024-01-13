# https://school.programmers.co.kr/learn/courses/30/lessons/176963

def solution(name, yearning, photo):
    result_list = []
    
    for i in photo:
        result = 0
        
        for j in i:
            if j in name:
                result += yearning[name.index(j)]
                
        result_list.append(result)
        
    return result_list