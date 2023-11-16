# https://school.programmers.co.kr/learn/courses/30/lessons/181934

def solution(ineq, eq, n, m):
    if eq == "!":
        answer = int(eval(str(n) + ineq + str(m)))
    else:
        answer = int(eval(str(n) + ineq + eq + str(m)))

    return answer