# https://school.programmers.co.kr/learn/courses/30/lessons/120864

def solution(my_string):
    check = str.maketrans("bcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    
    my_string = my_string.translate(check)
    
    return sum([int(i) for i in my_string.split("a") if not i == ""])