# https://school.programmers.co.kr/learn/courses/30/lessons/142086

def solution(s):
    result = []
    alphabet_set = set(list(s))
    alphabet_dict = {}
    
    for i in alphabet_set:
        alphabet_dict[i] = s.index(i)
        
    for i in range(len(s)):
        if i == alphabet_dict[s[i]]:
            result.append(-1)
        else:
            result.append(i - alphabet_dict[s[i]])
            
            alphabet_dict[s[i]] = i
            
    return result