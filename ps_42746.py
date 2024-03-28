# https://school.programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    numbers = [str(i) for i in numbers]
    numbers.sort(key = lambda x: (x * 4)[: 4], reverse = True)
    
    if numbers[0] == '0':
        answer = '0'
    else:
        answer = ''.join(numbers)
        
    return answer