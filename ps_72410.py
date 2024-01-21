# https://school.programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    result = ""
    
    check_point = 0
    ban_character = "~!@#$%^&*()=+[{]}:?,<>/"
    
    new_id = new_id.lower()
    
    for i in new_id:
        if i == ".":
            if result == "" or result[-1] == ".":
                continue
            else:
                result += i   
        elif not i in ban_character:
            result += i
        
    if result == "":
        result = "aaa"
    
    if result[-1] == ".":
        result = result[: -1]
        
    if len(result) >= 16:
        if result[14] == ".":
            result = result[: 14]
        else:
            result = result[: 15]
            
    if len(result) <= 2:
        while len(result) < 3:
            result += result[-1]
            
    return result