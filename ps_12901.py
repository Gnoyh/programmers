# https://school.programmers.co.kr/learn/courses/30/lessons/12901

def solution(a, b):
    day_list = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    week_list = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    
    return week_list[(sum(day_list[: a]) + b) % 7]