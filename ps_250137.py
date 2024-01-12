# https://school.programmers.co.kr/learn/courses/30/lessons/250137

def solution(bandage, health, attacks):
    now_time = 0
    now_health = health
    
    for i in attacks:
        if now_health <= 0:
            return -1
        
        if now_health == health:
            now_time = i[0]
            now_health -= i[1]
            
            continue
            
        bandage_time = i[0] - now_time - 1
        
        while bandage_time >= bandage[0]:
            now_health = min(health, now_health + (bandage[0] * bandage[1]) + bandage[2])
            
            if now_health == health:
                break
            
            bandage_time -= bandage[0]
        
        if now_health < health and bandage_time > 0:
            now_health = min(health, now_health + (bandage_time * bandage[1]))
            
        now_time = i[0]
        now_health -= i[1]
            
    if now_health <= 0:
        return -1
    else:
        return now_health