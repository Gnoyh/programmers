# https://school.programmers.co.kr/learn/courses/30/lessons/181870

def solution(strArr):
    for i in strArr[: ]:
        if "ad" in i:
            strArr.remove(i)
    
    return strArr