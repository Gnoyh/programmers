# https://school.programmers.co.kr/learn/courses/30/lessons/258712

def solution(friends, gifts):
    exponent_list = [0] * len(friends)
    record_list = [0] * (len(friends) * (len(friends) - 1))
    result_list = [0] * len(friends)
    
    for i in gifts:
        friend = i.split()
        
        exponent_list[friends.index(friend[0])] += 1
        exponent_list[friends.index(friend[1])] -= 1
        
        for j in friends:
            if j == friend[0]:
                record_list[(friends.index(friend[0]) * len(friends)) + friends.index(friend[1])] += 1
                
                break
            elif j == friend[1]:
                record_list[(friends.index(friend[1]) * len(friends)) + friends.index(friend[0])] -= 1
                
                break
                
    for i in range(1, len(record_list)):
        friend_give = i // len(friends)
        friend_take = i % len(friends)
        
        if friend_give >= friend_take:
            continue
        
        if record_list[i] > 0:
            result_list[friend_give] += 1
        elif record_list[i] < 0:
            result_list[friend_take] += 1
        else:
            if exponent_list[friend_give] > exponent_list[friend_take]:
                result_list[friend_give] += 1
            elif exponent_list[friend_give] < exponent_list[friend_take]:
                result_list[friend_take] += 1
                
    return max(result_list)