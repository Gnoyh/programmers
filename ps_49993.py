# https://school.programmers.co.kr/learn/courses/30/lessons/49993

def solution(skill, skill_trees):
    result = 0
    possible_tree = [""]
    
    for i in range(len(skill), 0, -1):
        possible_tree.append(skill[: i])
        
    for i, v in enumerate(skill_trees):
        new_trees = ""
        
        for j in v:
            if j in skill:
                new_trees += j
                
        if new_trees in possible_tree:
            result += 1
            
    return result