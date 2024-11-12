# https://school.programmers.co.kr/learn/courses/30/lessons/340213

def change_min(s):
    return int(s[: 2]) * 60 + int(s[3: ])

def solution(video_len, pos, op_start, op_end, commands):
    video_min = change_min(video_len)
    pos_min = change_min(pos)
    start_min = change_min(op_start)
    end_min = change_min(op_end)
    
    for i in commands:
        if pos_min <= end_min and pos_min >= start_min:
            pos_min = end_min
            
        if i == 'prev':
            pos_min = max(0, pos_min - 10)
        else:
            pos_min = min(video_min, pos_min + 10)
            
    if pos_min <= end_min and pos_min >= start_min:
        pos_min = end_min
        
    result = f"{(pos_min // 60):02d}:{(pos_min % 60):02d}"
    
    return result