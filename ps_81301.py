# https://school.programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    number_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for i, v in enumerate(number_list):
        if s.isdigit():
            return int(s)
        
        s = s.replace(v, str(i))
    
    return int(s)