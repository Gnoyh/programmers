# https://school.programmers.co.kr/learn/courses/30/lessons/12977

def solution(nums):
    result = 0
    pn_list = [0] * 2998
    
    for i in range(2, 2998):
        if pn_list[i] == 0:
            for j in range(i * 2, 2998, i):
                pn_list[j] = 1
    
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if pn_list[nums[i] + nums[j] + nums[k]] == 0:
                    result += 1
                    
    return result