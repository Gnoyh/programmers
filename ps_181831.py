# https://school.programmers.co.kr/learn/courses/30/lessons/181831

def solution(arr):
    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i][j] != arr[j][i]:
                return 0
            
    return 1