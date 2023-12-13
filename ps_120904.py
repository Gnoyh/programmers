https://school.programmers.co.kr/learn/courses/30/lessons/120904

def solution(num, k):
    if str(num).find(str(k)) == -1:
        return str(num).find(str(k))
    else:
        return str(num).find(str(k)) + 1