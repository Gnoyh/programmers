# https://school.programmers.co.kr/learn/courses/30/lessons/49994

def solution(dirs):
    x = 0
    y = 0
    
    check_list = []
    
    for i in dirs:
        if i == 'U' and y < 5:
            check_list.append((x, y, 'U'))
            
            y += 1
            
            check_list.append((x, y, 'D'))
        elif i == 'D' and y > -5:
            check_list.append((x, y, 'D'))
            
            y -= 1
            
            check_list.append((x, y, 'U'))
        elif i == 'R' and x < 5:
            check_list.append((x, y, 'R'))
            
            x += 1
            
            check_list.append((x, y, 'L'))
        elif i == 'L' and x > -5:
            check_list.append((x, y, 'L'))
            
            x -= 1
            
            check_list.append((x, y, 'R'))
            
    return len(set(check_list)) // 2