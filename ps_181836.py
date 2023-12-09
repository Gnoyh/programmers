# https://school.programmers.co.kr/learn/courses/30/lessons/181836

def solution(picture, k):
    result = []
    
    for i in picture:
        check = ""
        
        for j in i:
            check += j * k
            
        for j in range(k):
            result.append(check)
        
    return result