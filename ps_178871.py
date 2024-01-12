# https://school.programmers.co.kr/learn/courses/30/lessons/178871

def solution(players, callings):
    ranking_list = {}
    
    for i in range(len(players)):
        ranking_list[players[i]] = i
        
    for i in callings:
        rank = ranking_list[i]
        
        ranking_list[players[rank - 1]], ranking_list[players[rank]] = ranking_list[players[rank]], ranking_list[players[rank - 1]]
        
        players[rank - 1], players[rank] = players[rank], players[rank - 1]
        
    return players