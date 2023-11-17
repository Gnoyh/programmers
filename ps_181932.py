# https://school.programmers.co.kr/learn/courses/30/lessons/181932

def solution(code):
    answer = ''
    mode = 0

    for i in range(len(code)):
        if code[i] == "1":
            mode = abs(mode - 1)

            continue

        if mode == 0:
            if i % 2 == 0:
                answer += code[i]
        else:
            if i % 2 == 1:
                answer += code[i]

    if answer == "":
        return "EMPTY"

    return answer