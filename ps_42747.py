# https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    citations.sort(reverse=True)
    
    for i, v in enumerate(citations):
        if v <= i + 1:
            return max(v, i)

    return len(citations)