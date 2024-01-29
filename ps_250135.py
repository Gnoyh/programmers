# https://school.programmers.co.kr/learn/courses/30/lessons/250135

def check_time(t, n):
    if t % n == 0:
        return n
    else:
        return t % n

def solution(h1, m1, s1, h2, m2, s2):
    result = 0

    t1 = h1 * 3600 + m1 * 60 + s1
    t2 = h2 * 3600 + m2 * 60 + s2

    for i in range(1, t2 - t1 + 1):
        if check_time(t1 + i - 1, 43200) >= ((s1 + i - 1) % 60) * 720 and check_time(t1 + i, 43200) < check_time(s1 + i, 60) * 720:
            result += 1

        if check_time(t1 + i - 1, 3600) >= ((s1 + i - 1) % 60) * 60 and check_time(t1 + i, 3600) < check_time(s1 + i, 60) * 60:
            result += 1

        if (t1 + i - 1) % 43200 == 0:
            result -= 1

    if check_time(t2, 3600) == check_time(s2, 60) * 60:
        result += 1

    return result