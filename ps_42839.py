# https://school.programmers.co.kr/learn/courses/30/lessons/42839

def solution(numbers):
    num_dict = dict()
    num_list = []
    
    for i in numbers:
        num_dict[i] = num_dict.get(i, 0) + 1
        
        num_list.append(str(i))
        
    num_list.sort(reverse = True)
    
    max_num = int("".join(num_list))
    
    prime_list = [i for i in range(max_num + 1)]
    
    prime_list[0] = 0
    prime_list[1] = 0
    
    for i in range(2, int(max_num ** (0.5)) + 1):
        if prime_list[i] == 0:
            continue
        else:
            for j in range(i ** 2, max_num + 1, i):
                prime_list[j] = 0
        
    prime_set = set(prime_list)
    
    prime_set.discard(0)
    
    prime_num = list(prime_set)
    
    result = 0
    
    for i in prime_num:
        check_dict = dict()
        check_num = str(i)
        
        for j in check_num:
            check_dict[j] = check_dict.get(j, 0) + 1
            
        result += 1
        
        for j in check_dict:
            if check_dict[j] > num_dict.get(j, 0):
                result -= 1
                
                break
                
    return result