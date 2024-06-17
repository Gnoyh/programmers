# https://school.programmers.co.kr/learn/courses/30/lessons/12949

def solution(arr1, arr2):
    result = [[] for i in range(len(arr1))]
    
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            check = 0
            
            for k in range(len(arr1[0])):
                check += arr1[i][k] * arr2[k][j]
                
            result[i].append(check)
        
    return result