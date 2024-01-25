# https://school.programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    word_list = s.split(" ")
    
    for i, v in enumerate(word_list):
        change_word = ""
        
        for j, w in enumerate(v):
            if j % 2 == 0:
                change_word += w.upper()
            else:
                change_word += w.lower()
        
        word_list[i] = change_word
        
    return " ".join(word_list)