# https://school.programmers.co.kr/learn/courses/30/lessons/181187

def solution(r1, r2):
    result = 0

    for i in range(1, r2):
        result += int((r2 ** 2 - i ** 2) ** 0.5)

    for i in range(1, r1):
        if int((r1 ** 2 - i ** 2) ** 0.5) == (r1 ** 2 - i ** 2) ** 0.5:
            result -= int((r1 ** 2 - i ** 2) ** 0.5) - 1
        else:
            result -= int((r1 ** 2 - i ** 2) ** 0.5)

    return (result + r2 - r1 + 1) * 4