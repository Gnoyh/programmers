# https://school.programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    result = []
    id_dict = dict()
    
    for i in record:
        record_list = i.split()
        
        if record_list[0] != "Leave":
            id_dict[record_list[1]] = record_list[2]
            
    for i in record:
        record_list = i.split()
        
        if record_list[0] == "Enter":
            result.append(id_dict[record_list[1]] + "님이 들어왔습니다.")
        elif record_list[0] == "Leave":
            result.append(id_dict[record_list[1]] + "님이 나갔습니다.")
    
    return result