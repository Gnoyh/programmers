# https://school.programmers.co.kr/learn/courses/30/lessons/181834

def solution(myString):
    result = ""
    
    for i in myString:
        if ord(i) < ord("l"):
            result += "l"
        else:
            result += i
            
    return result