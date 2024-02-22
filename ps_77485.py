# https://school.programmers.co.kr/learn/courses/30/lessons/77485

def solution(rows, columns, queries):
    result = []
    
    move_list = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    rc_list = [[i * columns + j for j in range(1, columns + 1)] for i in range(rows)]
    
    for i in queries:
        move = 0
        x = i[0] - 1
        y = i[1] - 1
        
        idx_list = [[x, y]]
        int_list = [rc_list[x][y]]
        
        while move < 4:
            if i[0] - 1 <= x + move_list[move][1] < i[2] and i[1] - 1 <= y + move_list[move][0] < i[3]:
                x += move_list[move][1]
                y += move_list[move][0]
                
                idx_list.append([x, y])
                int_list.append(rc_list[x][y])
            else:
                move += 1
                
        idx_list.pop()
        int_list = [int_list[-2]] + int_list[: -2]
        
        result.append(min(int_list))
        
        for j in range(len(idx_list)):
            rc_list[idx_list[j][0]][idx_list[j][1]] = int_list[j]
            
    return result