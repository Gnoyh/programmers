# https://school.programmers.co.kr/learn/courses/30/lessons/181859

def solution(arr):
    stk = []
    
    for i in range(len(arr)):
        if len(stk) == 0:
            stk.append(arr[i])
        elif stk[-1] == arr[i]:
            stk.pop()
        else:
            stk.append(arr[i])
    
    return stk if len(stk) != 0 else [-1]