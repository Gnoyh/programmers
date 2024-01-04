# https://school.programmers.co.kr/learn/courses/30/lessons/120839

def solution(rsp):
    check_list = ["5", "-1", "0", "-1", "-1", "2"]
    
    return "".join([check_list[int(i)] for i in rsp])