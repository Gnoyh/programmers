# https://school.programmers.co.kr/learn/courses/30/lessons/120907

def solution(quiz):
    quiz = [i.replace("=", "==") for i in quiz]
    
    return ["O" if eval(i) else "X" for i in quiz]