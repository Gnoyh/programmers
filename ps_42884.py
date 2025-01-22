# https://school.programmers.co.kr/learn/courses/30/lessons/42884

def solution(routes):
    result = 1
    
    routes.sort(key = lambda x: (x[1], x[0]))
    
    check = routes[0][1]
    
    for i in routes:
        if i[0] <= check and check <= i[1]:
            continue
        else:
            result += 1
            check = i[1]
    
    return result