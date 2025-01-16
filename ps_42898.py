# https://school.programmers.co.kr/learn/courses/30/lessons/42898

def solution(m, n, puddles):
    visited = [[0 for i in range(n + 1)] for j in range(m + 1)]
    move = [[1, 0], [0, 1]]
    check_list = [1001]
    
    for i in puddles:
        visited[i[0]][i[1]] = -1
    
    visited[1][1] = 1
    
    while check_list != []:
        check_dict = dict()
        new_list = []
        
        for i in check_list:
            for j in move:
                x = i // 1000 + j[0]
                y = i % 1000 + j[1]
                num = x * 1000 + y
                
                if x > m or y > n:
                    continue
                
                if visited[x][y] == 0:
                    check_dict[num] = check_dict.get(num, 0) + visited[i // 1000][i % 1000]
                    
        for i in check_dict:
            visited[i // 1000][i % 1000] = check_dict[i]
            new_list.append(i)
            
        check_list = new_list
        
    return visited[m][n] % 1000000007