# https://school.programmers.co.kr/learn/courses/30/lessons/154539

def solution(numbers):
    result = [-1]
    max_list = [numbers[-1]]
    
    for i in range(len(numbers) - 2, -1, -1):
        if numbers[i] < max_list[0]:
            while numbers[i] >= max_list[-1]:
                max_list.pop()
                
            result.append(max_list[-1])
            max_list.append(numbers[i])
        else:
            max_list = [numbers[i]]
            
            result.append(-1)
            
    return result[: : -1]