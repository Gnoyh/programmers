# https://school.programmers.co.kr/learn/courses/30/lessons/181862

def solution(myStr):
    myStr = myStr.replace("b", "a").replace("c", "a")
    
    if set(list(myStr)) == {"a"}:
        return ["EMPTY"]
    
    return [i for i in myStr.split("a") if i != ""]