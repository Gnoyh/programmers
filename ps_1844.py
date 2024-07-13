from collections import deque

def solution(maps):
    n = len(maps[0]) - 1
    m = len(maps) - 1
    
    moved = deque([[0, 0, 1]])
    
    maps[0][0] = 0

    def move(i, j, count):
        if j + 1 <= n and maps[i][j + 1] == 1:
            moved.append([i, j + 1, count + 1])
            
            maps[i][j + 1] = count + 1
        
        if i + 1 <= m and maps[i + 1][j] == 1:
            moved.append([i + 1, j, count + 1])
            
            maps[i + 1][j] = count + 1
        
        if 0 <= j - 1 and maps[i][j - 1] == 1:
            moved.append([i, j - 1, count + 1])
            
            maps[i][j - 1] = count + 1
        
        if 0 <= i - 1 and maps[i - 1][j] == 1:
            moved.append([i - 1, j, count + 1])
            
            maps[i - 1][j] = count + 1
                
    while moved:
        now = moved.popleft()
        
        move(now[0], now[1], now[2])
        
        if maps[m][n] != 1:
            return maps[m][n]
        
    return -1