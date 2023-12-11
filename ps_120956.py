# https://school.programmers.co.kr/learn/courses/30/lessons/120956

def solution(babbling):
    check_list = ["aya", "ye", "woo", "ma"]
    result = 0

    for i in babbling:
        for j in check_list:
            i = i.replace(j, " ").strip()
            
        if i == "":
            result += 1

    return result