# https://school.programmers.co.kr/learn/courses/30/lessons/86052

def solution(grid):
    result = []
    
    move_list = [[-1, 0], [0, -1], [0, 1], [1, 0]]
    visited_list = [[[0] * 4 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    
    move_dict = {"S": [0, 1, 2, 3], "L": [1, 3, 0, 2], "R": [2, 0, 3, 1]}
    
    for i in range(len(grid)):
        for j in range(len(grid)):
            for k in range(4):
                if visited_list[i][j][k] == 0:
                    visited_list[i][j][k] = 1
                    ci = (len(grid) + i + move_list[k][0]) % len(grid)
                    cj = (len(grid[0])+ j + move_list[k][1]) % len(grid[0])
                    ck = k
                    count = 0
                
                    while visited_list[ci][cj][ck] == 0:
                        visited_list[ci][cj][ck] = 1
                        
                        ck = move_dict[]
                        ci += (len(grid) + move_dict[grid[ci][cj][ck]][ck][0]) % len(grid)
                        cj += move_list[ck][1]
                    
                        count += 1
                    
                    