# https://school.programmers.co.kr/learn/courses/30/lessons/92341

def solution(fees, records):
    records = [i.split() for i in records]
    car_list = sorted(list({i[1] for i in records}))
    car_time = {}
    
    for i in car_list:
        car_time[i] = 0
    
    result = [0] * len(car_list)
    
    for i in records:
        time = int(i[0].split(":")[0]) * 60 + int(i[0].split(":")[1])
        
        if i[2] == "IN":
            car_time[i[1]] -= time
        else:
            car_time[i[1]] += time
            
    for k, v in car_time.items():
        if v <= 0:
            v += 1439
        
        if v <= fees[0]:
            result[car_list.index(k)] += fees[1]
        else:
            if (v - fees[0]) % fees[2] == 0:
                result[car_list.index(k)] += fees[1] + ((v - fees[0]) // fees[2]) * fees[3]
            else:
                result[car_list.index(k)] += fees[1] + ((v - fees[0]) // fees[2] + 1) * fees[3]
                
    return result