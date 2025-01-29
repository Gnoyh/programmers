# https://school.programmers.co.kr/learn/courses/30/lessons/12971

def solution(sticker):
    if len(sticker) <= 3:
        return max(sticker)
    else:
        check_list = [[0, 0] for _ in range(len(sticker))]
        
        check_list[0][0] = sticker[0]
        check_list[1][0] = sticker[0]
        check_list[1][1] = sticker[1]
        
        for i in range(2, len(sticker)):
            check_list[i][0] = max(check_list[i - 2][0] + sticker[i], check_list[i - 1][0])
            check_list[i][1] = max(check_list[i - 2][1] + sticker[i], check_list[i - 1][1])
        
        return max(check_list[-2][0], check_list[-1][1])