# https://school.programmers.co.kr/learn/courses/30/lessons/120849

def solution(my_string):
    result = ""
    
    for i in my_string:
        if not i in ["a", "e", "i", "o", "u"]:
            result += i
            
    return result