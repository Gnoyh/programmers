# https://school.programmers.co.kr/learn/courses/30/lessons/181864

def solution(myString, pat):
    new_pat = ""
    
    for i in pat:
        if i == "A":
            new_pat += "B"
        else:
            new_pat += "A"
            
    return int(new_pat in myString)