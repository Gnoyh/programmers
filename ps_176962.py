# https://school.programmers.co.kr/learn/courses/30/lessons/176962

def solution(plans):
    result = []
    
    new_plans = []
    stop_plans = []
    
    for i in plans:
        time = i[1].split(":")
        
        new_plans.append([i[0], int(time[0]) * 60 + int(time[1]), int(i[2])])
        
    new_plans.sort(key = lambda x: x[1])
    
    start_time = new_plans[0][1]
    
    for i in range(1, len(new_plans)):
        check_time = new_plans[i][1] - start_time
        start_time = new_plans[i][1]
        
        if check_time == new_plans[i - 1][2]:
            result.append(new_plans[i - 1][0])
        elif check_time < new_plans[i - 1][2]:
            stop_plans.append([new_plans[i - 1][0], new_plans[i - 1][2] - check_time])
        else:
            result.append(new_plans[i - 1][0])
            
            check_time -= new_plans[i - 1][2]
            
            if len(stop_plans) > 0:
                for j in range(len(stop_plans) -1, -1, -1):
                    if stop_plans[j][1] <= check_time:
                        result.append(stop_plans[j][0])
                        
                        check_time -= stop_plans[j][1]
                        
                        stop_plans.pop()
                    else:
                        stop_plans[j][1] -= check_time
                        
                        break
            
    result.append(new_plans[-1][0])
    
    for i in stop_plans[: : -1]:
        result.append(i[0])
        
    return result