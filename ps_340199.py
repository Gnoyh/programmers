# https://school.programmers.co.kr/learn/courses/30/lessons/340199

def solution(wallet, bill):
    result = 0
    
    while max(wallet) < max(bill) or min(wallet) < min(bill):
        if bill[0] >= bill[1]:
            bill[0] //= 2
        else:
            bill[1] //= 2
            
        result += 1
        
    return result