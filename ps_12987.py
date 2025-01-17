# https://school.programmers.co.kr/learn/courses/30/lessons/12987

def solution(A, B):
    result = 0
    
    A.sort(reverse = True)
    B.sort(reverse = True)
    
    idx = 0
    
    for i in A:
        if i >= B[idx]:
            B.pop()
        else:
            idx += 1
            result += 1
            
    return result