# https://school.programmers.co.kr/learn/courses/30/lessons/120880

def solution(numlist, n):
    numlist = [(abs(i - n), i) for i in numlist]
    
    numlist.sort(key = lambda x: (x[0], -x[1]))
    
    return [i[1] for i in numlist]

