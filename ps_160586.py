# https://school.programmers.co.kr/learn/courses/30/lessons/160586

def solution(keymap, targets):
    result_list = []
    alphabet_list = {"A": 101, "B": 101, "C": 101, "D": 101, "E": 101, "F": 101, "G": 101, "H": 101, "I": 101, "J": 101, "K": 101, "L": 101, "M": 101, "N": 101, "O": 101, "P": 101, "Q": 101, "R": 101, "S": 101, "T": 101, "U": 101, "V": 101, "W": 101, "X": 101, "Y": 101, "Z": 101}
    
    for i in alphabet_list:
        for j in keymap:
            if i in j:
                alphabet_list[i] = min(alphabet_list[i], j.index(i) + 1)
    
    for i in targets:
        result = 0
        
        for j in i:
            if alphabet_list[j] == 101:
                result = -1
                
                break
            else:
                result += alphabet_list[j]
            
        
        result_list.append(result)
        
    return result_list