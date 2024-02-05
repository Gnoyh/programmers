# https://school.programmers.co.kr/learn/courses/30/lessons/150368

from itertools import product

def solution(users, emoticons):
    result = [0, 0]
    
    discount_list = [10, 20, 30, 40]
        
    for i in list(product(discount_list, repeat = len(emoticons))):
        count_ep = 0
        count_total = 0
        
        for j in users:
            total = 0
            
            for k in range(len(i)):
                if j[0] <= i[k]:
                    total += (emoticons[k] * (100 - i[k])) // 100
                    
            if j[1] <= total:
                count_ep += 1
            else:
                count_total += total
                
        if count_ep > result[0]:
            result = [count_ep, count_total]
        elif count_ep == result[0]:
            result = [count_ep, max(result[1], count_total)]
            
    return result