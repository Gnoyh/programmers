# https://school.programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    def cal(i, temp):
        p = temp + numbers[i]
        m = temp - numbers[i]
        
        if i == len(numbers) - 1:
            if p == target or m == target:
                return 1
            else:
                return 0
        else:
            return cal(i + 1, m) + cal(i + 1, p)
        
    return cal(0, 0)