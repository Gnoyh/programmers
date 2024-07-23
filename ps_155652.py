# https://school.programmers.co.kr/learn/courses/30/lessons/155652

def solution(s, skip, index):
    result = ""
    
    alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    
    for i in skip:
        alphabet_list.remove(i)
        
    for i in s:
        result += alphabet_list[(alphabet_list.index(i) + index) % len(alphabet_list)]
        
    return result