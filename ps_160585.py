# https://school.programmers.co.kr/learn/courses/30/lessons/160585

def solution(board):
    o_count = 0
    x_count = 0
    
    finish_o = 0
    finish_x = 0
    
    for i in board:
        for j in i:
            if j == "O":
                o_count += 1
            elif j == "X":
                x_count += 1
        
    if o_count - x_count == 0:
        finish_x = 1
    elif o_count - x_count == 1:
        finish_o = 1
    else:
        return 0
    
    for i in range(3):
        if board[i] == "OOO":
            if finish_x == 1:
                return 0
        elif board[i] == "XXX":
            if finish_o == 1:
                return 0
            
        if board[0][i] + board[1][i] + board[2][i] == "OOO":
            if finish_x == 1:
                return 0
        elif board[0][i] + board[1][i] + board[2][i] == "XXX":
            if finish_o == 1:
                return 0
            
    if board[0][0] + board[1][1] + board[2][2] == "OOO" or board[0][2] + board[1][1] + board[2][0] == "OOO":
        if finish_x == 1:
            return 0
    elif board[0][0] + board[1][1] + board[2][2] == "XXX" or board[0][2] + board[1][1] + board[2][0] == "XXX":
        if finish_o == 1:
            return 0
        
    return 1