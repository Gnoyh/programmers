# https://school.programmers.co.kr/learn/courses/30/lessons/120871

def solution(n):
    check_list = [0] * 100
    count = 0
    check = 1
    
    while count < n:
        if "3" in str(check) or check % 3 == 0:
            check += 1
        else:
            check_list[count] = check
            
            count += 1
            check += 1
            
    return check_list[n - 1]