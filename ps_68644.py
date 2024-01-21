# https://school.programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers):
    result_set = set()
    
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            result_set.add(numbers[i] + numbers[j])
            
    return sorted(list(result_set))