# https://school.programmers.co.kr/learn/courses/30/lessons/120808

def solution(numer1, denom1, numer2, denom2):
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    
    check = 2
    check_min = min(numer, denom)
    
    while check < check_min:
        if numer % check == 0 and denom % check == 0:
            numer //= check
            denom //= check
        else:
            check += 1
            
    return [numer, denom]