# https://school.programmers.co.kr/learn/courses/30/lessons/181883

def solution(arr, queries):
    for i, j in queries:
        for k in range(i, j + 1):
            arr[k] += 1
            
    return arr