# https://school.programmers.co.kr/learn/courses/30/lessons/181860

def solution(arr, flag):
    result_list = []
    
    for i in range(len(flag)):
        if flag[i]:
            result_list += [arr[i]] * arr[i] * 2
        else:
            for i in range(arr[i]):
                result_list.pop()
            
    return result_list