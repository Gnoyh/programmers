# https://school.programmers.co.kr/learn/courses/30/lessons/133502

def solution(ingredient):
    result = 0
    ingredient_list = []
    
    for i in ingredient:
        ingredient_list.append(i)
        
        if ingredient_list[-4: ] == [1, 2, 3, 1]:
            result += 1
            
            for j in range(4):
                ingredient_list.pop()
                
    return result