# https://school.programmers.co.kr/learn/courses/30/lessons/181830

def solution(arr):
    if len(arr[0]) > len(arr):
        for i in range(len(arr[0]) - len(arr)):
            arr.append([0] * len(arr[0]))
    elif len(arr[0]) < len(arr):
        for i in range(len(arr)):
            arr[i] += [0] * (len(arr) - len(arr[-1]))
    
    return arr