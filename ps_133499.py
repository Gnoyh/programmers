# https://school.programmers.co.kr/learn/courses/30/lessons/133499

def solution(babbling):
    result = 0
    
    for i in babbling:
        i = i.replace("aya", "1").replace("ye", "2").replace("woo", "3").replace("ma", "4")
        
        if i.isdigit() and not "11" in i and not "22" in i and not "33" in i and not "44" in i:
            result += 1
            
    return result