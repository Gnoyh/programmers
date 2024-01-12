# https://school.programmers.co.kr/learn/courses/30/lessons/250125

def solution(board, h, w):
    result = 0
    
    if h - 1 >= 0:
        if board[h][w] == board[h - 1][w]:
            result += 1
    
    if h + 1 < len(board):
        if board[h][w] == board[h + 1][w]:
            result += 1
    
    if w - 1 >= 0:
        if board[h][w] == board[h][w - 1]:
            result += 1
    
    if w + 1 < len(board):
        if board[h][w] == board[h][w + 1]:
            result += 1
            
    return result