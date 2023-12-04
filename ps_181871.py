# https://school.programmers.co.kr/learn/courses/30/lessons/181871

def solution(myString, pat):
    result_num = 0
    
    for i in range(len(myString) - len(pat) + 1):
        if pat == myString[i: i + len(pat)]:
            result_num += 1
            
    return result_num