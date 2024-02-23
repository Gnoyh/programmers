# https://school.programmers.co.kr/learn/courses/30/lessons/72412

def solution(info, query):
    result = []
    
    info_dict = {}
    
    for i in ["-", "cpp", "java", "python"]:
        for j in ["-", "backend", "frontend"]:
            for k in ["-", "junior", "senior"]:
                for l in ["-", "chicken", "pizza"]:
                    info_dict[i + j + k + l] = []
                    
    for h in info:
        split_info = h.split()
        
        for i in ["-", split_info[0]]:
            for j in ["-", split_info[1]]:
                for k in ["-", split_info[2]]:
                    for l in ["-", split_info[3]]:
                        info_dict[i + j + k + l].append(int(split_info[4]))
                        
    for i in info_dict:
        info_dict[i].sort(reverse = True)
        
    for i in query:
        query_info = i.replace("and", "").split()
        
        check_info = "".join(query_info[: -1])
        check_score = int(query_info[-1])
        
        if not info_dict[check_info] or info_dict[check_info][0] < check_score:
            result.append(0)
        elif info_dict[check_info][-1] >= check_score:
            result.append(len(info_dict[check_info]))
        else:
            start = 0
            end = len(info_dict[check_info]) - 1
            
            while start + 1 < end:
                idx = (start + end) // 2
                
                if info_dict[check_info][idx] >= check_score:
                    start = idx
                elif info_dict[check_info][idx] < check_score:
                    end = idx
                        
            result.append(start + 1)
            
    return result