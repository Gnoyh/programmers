# https://school.programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    result_list = []
    
    for i in number:
        while result_list and result_list[-1] < i and k > 0:
            result_list.pop()
            
            k -= 1
            
        result_list.append(i)
        
    result = "".join(result_list[: len(result_list) - k])
    
    return result