# https://school.programmers.co.kr/learn/courses/30/lessons/17677

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    str1_dict = {}
    str2_dict = {}
    
    result1 = 0
    result2 = 0
    
    for i in range(len(str1) - 1):
        if str1[i: i + 2].isalpha():
            str1_dict[str1[i: i + 2]] = str1_dict.get(str1[i: i + 2], 0) + 1
            
    for i in range(len(str2) - 1):
        if str2[i: i + 2].isalpha():
            str2_dict[str2[i: i + 2]] = str2_dict.get(str2[i: i + 2], 0) + 1
            
    for i in str1_dict:
        if str2_dict.get(i, 0) != 0:
            result1 += min(str1_dict[i], str2_dict[i])
            result2 += max(str1_dict[i], str2_dict[i])
        else:
            result2 += str1_dict[i]
            
    for i in str2_dict:
        if str1_dict.get(i, 0) == 0:
            result2 += str2_dict[i]
            
    if result2 != 0:
        return int(65536 * (result1 / result2))
    else:
        return 65536