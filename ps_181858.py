# https://school.programmers.co.kr/learn/courses/30/lessons/181858

def solution(arr, k):
    result_list = []
    
    for i in arr:
        if not result_list or i not in set(result_list):
            result_list.append(i)
            
        if len(result_list) == k:
            break
            
    return result_list + [-1] * (k - len(result_list))