# https://school.programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    result = []
    
    day_list = []
    
    for i, v in enumerate(progresses):
        if (100 - v) % speeds[i] == 0:
            day_list.append((100 - v) // speeds[i])
        else:
            day_list.append((100 - v) // speeds[i] + 1)
    
    max_day = day_list[0]
    count = 0
    
    for i in day_list:
        if i > max_day:
            result.append(count)
            max_day = i
            count = 1
        else:
            count += 1
            
    result.append(count)
            
    return result