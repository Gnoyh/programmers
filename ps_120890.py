# https://school.programmers.co.kr/learn/courses/30/lessons/120890

def solution(array, n):
    array.sort(key = lambda x: (abs(x - n), x - n))
    
    return array[0]