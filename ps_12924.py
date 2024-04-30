# vhttps://school.programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    result = 1
    check = 2
    
    while n >= (check * (check + 1)) // 2:
        if (n - (check * (check + 1)) // 2) % check == 0:
            result += 1
            
        check += 1
        
    return result