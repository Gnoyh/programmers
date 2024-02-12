# https://school.programmers.co.kr/learn/courses/30/lessons/92335

def solution(n, k):
    result = 0
    
    num = ""
    
    while n > 0:
        num = str(n % k) + num
        
        n //= k
    
    result_list = [int(i) for i in num.split("0") if i != ""]
    
    for i in result_list:
        if i > 1:
            check = 0
            count = 2
            
            while count ** 2 <= i:
                if i % count == 0:
                    check = 1
                    
                    break
                
                count += 1
                
            if check == 0:
                result += 1
                
    return result