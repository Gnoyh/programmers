# https://school.programmers.co.kr/learn/courses/30/lessons/181936

def solution(number, n, m):
    answer = int(number % n == 0 and number % m == 0)

    return answer