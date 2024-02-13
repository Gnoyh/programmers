# https://school.programmers.co.kr/learn/courses/30/lessons/87390

def solution(n, left, right):
    result = []
    
    left_q = left // n
    left_r = left % n
    right_q = right // n
    right_r = right % n
    
    if left_q == right_q:
        return [left_q + 1 if i <= left_q else i + 1 for i in range(left_r, right_r + 1)]
    
    result += [left_q + 1 if i <= left_q else i + 1 for i in range(left_r, n)]
    
    for i in range(left_q + 1, right_q):
        result += [i + 1 if j <= i else j + 1 for j in range(n)]
        
    result += [right_q + 1 if i <= right_q else i + 1 for i in range(right_r + 1)]
    
    return result