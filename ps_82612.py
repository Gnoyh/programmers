# https://school.programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    sum_price = sum([i for i in range(1, count + 1)]) * price
    
    if sum_price - money > 0:
        return sum_price - money
    else:
        return 0