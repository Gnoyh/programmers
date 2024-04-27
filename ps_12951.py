# https://school.programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    check = s.split(" ")
    
    for i in range(len(check)):
        if len(check[i]) > 1:
            check[i] = check[i][0].upper() + check[i][1: ].lower()
        elif len(check[i]) == 1:
            check[i] = check[i][0].upper()
        
    return " ".join(check)