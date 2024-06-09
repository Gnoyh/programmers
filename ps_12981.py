# https://school.programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    check_set = set()
    
    check_set.add(words[0])
    
    for i, v in enumerate(words[1: ]):
        if words[i][-1] == v[0] and v not in check_set:
            check_set.add(v)
        else:
            return [(i + 1) % n + 1, (i + 1) // n + 1]
    
    return [0, 0]