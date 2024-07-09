# https://school.programmers.co.kr/learn/courses/30/lessons/43162

def solution(n, computers):
    check_list = [-1 for _ in range(n)]
    result = 0
    i = 0
    visited = set()
    
    def d(a, b):
        for i in range(n):
            if i not in visited and computers[a][i] == 1:
                visited.add(i)
                check_list[i] = b
                
                d(i, b)
    
    while i < len(computers):
        if check_list[i] == -1:
            visited.add(i)
            check_list[i] = result
            
            d(i, result)
            result += 1
            
        i += 1
            
    return result