# https://school.programmers.co.kr/learn/courses/30/lessons/169198

def solution(m, n, startX, startY, balls):
    result = []

    for i in balls:
        if startY == i[1]:
            if startX < i[0]:
                result.append(min((startX - i[0]) ** 2 + (2 * n - startY - i[1]) ** 2, (startX - i[0]) ** 2 + (-1 * startY - i[1]) ** 2, (startX + i[0]) ** 2))
            else:
                result.append(min((startX - i[0]) ** 2 + (2 * n - startY - i[1]) ** 2, (startX - i[0]) ** 2 + (-1 * startY - i[1]) ** 2, (2 * m - startX - i[0]) ** 2))
        elif startX == i[0]:
            if startY < i[1]:
                result.append(min((2 * m - startX - i[0]) ** 2 + (startY - i[1]) ** 2, (-1 * startX - i[0]) ** 2 + (startY - i[1]) ** 2, (startY + i[1]) ** 2))
            else:
                result.append(min((2 * m - startX - i[0]) ** 2 + (startY - i[1]) ** 2, (-1 * startX - i[0]) ** 2 + (startY - i[1]) ** 2, (2 * n - startY - i[1]) ** 2))
        else:
            result.append(min((startX - i[0]) ** 2 + (2 * n - startY - i[1]) ** 2, (startX - i[0]) ** 2 + (-1 * startY - i[1]) ** 2, (2 * m - startX - i[0]) ** 2 + (startY - i[1]) ** 2, (-1 * startX - i[0]) ** 2 + (startY - i[1]) ** 2))

    return result