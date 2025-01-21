# https://school.programmers.co.kr/learn/courses/30/lessons/17679

def solution(m, n, board):
    new_board = [""] * n
        
    for i in range(n):
        for j in range(m - 1, -1, -1):
            new_board[i] += board[j][i]
            
    result = 0
    
    while True:
        del_set = set()
        
        for i in range(n - 1):
            result += new_board[i].count("0")
            
            for j in range(m - 1):
                if new_board[i][j] != "0" and new_board[i][j] == new_board[i + 1][j] and new_board[i][j] == new_board[i][j + 1] and new_board[i][j] == new_board[i + 1][j + 1]:
                    del_set.add((i, j))
                    del_set.add((i + 1, j))
                    del_set.add((i, j + 1))
                    del_set.add((i + 1, j + 1))
                    
        result += new_board[n - 1].count("0")
        
        if del_set:
            for i in del_set:
                new_board[i[0]] = new_board[i[0]][: i[1]] + "0" + new_board[i[0]][i[1] + 1: ]
                
            for i in range(n):
                new_board[i] = new_board[i].replace("0", "")
                new_board[i] += "0" * (m - len(new_board[i]))
                
            result = 0
        else:
            break
        
    return result