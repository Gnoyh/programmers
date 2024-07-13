# https://school.programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque

def solution(maps):
    n = len(maps[0]) - 1
    m = len(maps) - 1
    
    visited = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    moved = deque([[0, 0, 1]])
    
    visited[0][0] = 1

    def move(i, j, count):
        if j + 1 <= n and maps[i][j + 1] and not visited[i][j + 1]:
            moved.append([i, j + 1, count + 1])
            visited[i][j + 1] = count + 1
        
        if i + 1 <= m and maps[i + 1][j] and not visited[i + 1][j]:
            moved.append([i + 1, j, count + 1])
            visited[i + 1][j] = count + 1
        
        if 0 <= j - 1 and maps[i][j - 1] and not visited[i][j - 1]:
            moved.append([i, j - 1, count + 1])
            visited[i][j - 1] = count + 1
        
        if 0 <= i - 1 and maps[i - 1][j] and not visited[i - 1][j]:
            moved.append([i - 1, j, count + 1])
            visited[i - 1][j] = count + 1
                
    while moved:
        now = moved.popleft()
        
        move(now[0], now[1], now[2])
        
        if visited[m][n] != 0:
            return visited[m][n]
        
    return -1