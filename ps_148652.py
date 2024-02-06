# https://school.programmers.co.kr/learn/courses/30/lessons/148652

def solution(n, l, r):
    result = r - l + 1

    for i in range(l - 1, r):
        check = i
        
        while check > 0:
            if check % 5 == 2:
                result -= 1
                
                break
            
            check //= 5
                
    return result