# https://school.programmers.co.kr/learn/courses/30/lessons/159994

def solution(cards1, cards2, goal):
    result = "Yes"
    cards1_index = 0
    cards2_index = 0
    
    for i in goal:
        if cards1_index < len(cards1) and i == cards1[cards1_index]:
            cards1_index += 1
        elif cards2_index < len(cards2) and i == cards2[cards2_index]:
            cards2_index += 1
        else:
            result = "No"
            
            break
            
    return result