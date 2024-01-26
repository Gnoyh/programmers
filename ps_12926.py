# https://school.programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    result = ""
    
    for i in s:
        if i == " ":
            result += " "
        elif i.isupper():
            result += chr((ord(i) + n - ord("A")) % 26 + ord("A"))
        else:
            result += chr((ord(i) + n - ord("a")) % 26 + ord("a"))
                
    return result