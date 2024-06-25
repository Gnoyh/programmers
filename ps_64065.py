# https://school.programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    check_dict = {}
    
    check_s = s.replace("{", "").replace("}", "").split(",")
    
    for i in check_s:
        i = int(i)
        
        check_dict[i] = check_dict.get(i, 0) + 1
            
    sorted_dict = sorted(check_dict.items(), key=lambda x: x[1], reverse=True)
            
    return [i[0] for i in sorted_dict]