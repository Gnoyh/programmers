# https://school.programmers.co.kr/learn/courses/30/lessons/161990

def solution(wallpaper):
    min_height = len(wallpaper)
    max_height = -1
    
    min_width = len(wallpaper[0])
    max_width = -1
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == "#":
                min_height = min(min_height, i)
                max_height = max(max_height, i)
                
                min_width = min(min_width, j)
                max_width = max(max_width, j)
                
    return [min_height, min_width, max_height + 1, max_width + 1]