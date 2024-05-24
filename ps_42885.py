# https://school.programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    result = 0
    s = 0
    e = len(people) - 1
    
    people.sort()
    
    while s <= e:
        if people[s] + people[e] <= limit and s != e:
            result += 1
            s += 1
            e -= 1
        else:
            result += 1
            e -= 1
            
    return result