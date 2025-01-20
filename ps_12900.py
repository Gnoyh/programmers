# https://school.programmers.co.kr/learn/courses/30/lessons/12900

def solution(n):
    fibo = [1, 1, 2]
    
    for i in range(3, n + 1):
        fibo.append((fibo[i - 2] % 1000000007) + (fibo[i - 1] % 1000000007))
        
    return fibo[n] % 1000000007