# https://school.programmers.co.kr/learn/courses/30/lessons/250121

def solution(data, ext, val_ext, sort_by):
    member_list = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    
    data = [i for i in data if i[member_list[ext]] < val_ext]
    
    data.sort(key = lambda x: x[member_list[sort_by]])
    
    return data