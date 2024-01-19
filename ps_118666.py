# https://school.programmers.co.kr/learn/courses/30/lessons/118666

def solution(survey, choices):
    result = ""
    
    personality_dict = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    
    for i in range(len(survey)):
        if choices[i] < 4:
            personality_dict[survey[i][0]] += 4 - choices[i]
        elif choices[i] > 4:
            personality_dict[survey[i][1]] += choices[i] - 4
            
    RCJA_list = ["R", "C", "J", "A"]
    TFMN_list = ["T", "F", "M", "N"]
    
    for i in range(4):
        if personality_dict[RCJA_list[i]] >= personality_dict[TFMN_list[i]]:
            result += RCJA_list[i]
        else:
            result += TFMN_list[i]
            
    return result