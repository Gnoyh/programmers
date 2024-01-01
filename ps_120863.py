# https://school.programmers.co.kr/learn/courses/30/lessons/120863

def solution(polynomial):
    check1 = 0
    check2 = 0

    for i in polynomial.split(" + "):
        if "x" in i:
            if i == "x":
                check1 += 1
            else:
                check1 += int(i[: -1])
        else:
            check2 += int(i)

    if check1 == 0:
        return str(check2)
    elif check2 == 0:
        if check1 == 1:
            return "x"
        else:
            return str(check1) + "x"
    else:
        if check1 == 1:
            return "x + " + str(check2)
        else:
            return str(check1) + "x + " + str(check2)