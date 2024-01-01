# https://school.programmers.co.kr/learn/courses/30/lessons/120861

def solution(keyinput, board):
    result = [0, 0]
    
    x = (board[0] - 1) // 2
    y = (board[1] - 1) // 2
    
    for i in keyinput:
        if i == "right":
            if result[0] < x:
                result[0] += 1
        elif i == "left":
            if result[0] > x * (-1):
                result[0] -= 1
        elif i == "up":
            if result[1] < y:
                result[1] += 1
        else:
            if result[1] > y * (-1):
                result[1] -= 1
                
    return result