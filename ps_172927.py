# https://school.programmers.co.kr/learn/courses/30/lessons/172927

def solution(picks, minerals):
    result = 0
    
    fatigue_list = []
    
    if sum(picks) * 5 < len(minerals):
        minerals = minerals[: sum(picks) * 5]
    
    for i in range(0, len(minerals) // 5 + 1):
        count_diamond = minerals[i * 5: min(i * 5 + 5, len(minerals))].count("diamond")
        count_iron = minerals[i * 5: min(i * 5 + 5, len(minerals))].count("iron")
        count_stone = minerals[i * 5: min(i * 5 + 5, len(minerals))].count("stone")
        
        fatigue_list.append([count_diamond + count_iron + count_stone, count_diamond * 5 + count_iron + count_stone, count_diamond * 25 + count_iron * 5 + count_stone])
        
    fatigue_list.sort(key = lambda x: -x[2])
    
    for i in fatigue_list:
        if picks[0] > 0:
            result += i[0]
            
            picks[0] -= 1
        elif picks[1] > 0:
            result += i[1]
            
            picks[1] -= 1
        elif picks[2] > 0:
            result += i[2]
            
            picks[2] -= 1
        else:
            break
            
    return result