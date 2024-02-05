# https://school.programmers.co.kr/learn/courses/30/lessons/148653

def solution(storey):
    result = 0

    while storey > 0:
        if storey % 10 > 5:
            result += 10 - (storey % 10)
            storey += 10 - (storey % 10)
        elif storey % 10 == 5:
            if (storey % 100) // 10 >= 5:
                result += 5
                storey += 5
            else:
                result += 5
        else:
            result += storey % 10

        storey //= 10

    return result