# https://school.programmers.co.kr/learn/courses/30/lessons/84512

def solution(word):
    result = 0
    
    count_list = [(5 ** i - 1) // 4 for i in range(5, 0, -1)]
    
    word_dict = {"A": 0, "E": 1, "I": 2, "O": 3, "U": 4}
    
    for i, v in enumerate(word):
        result += count_list[i] * word_dict[v] + 1
        
    return result