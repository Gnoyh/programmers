# https://school.programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    result = []
    
    genres_dict = {}
    result_list = []
    
    for i, v in enumerate(genres):
        genres_dict[v] = genres_dict.get(v, 0) + plays[i]
        
    for i, v in enumerate(sorted(list(genres_dict.items()), key = lambda x: -x[1])):
        genres_dict[v[0]] = i
        
    for i, v in enumerate(genres):
        result_list.append([genres_dict[v], plays[i], i])
        
    result_list.sort(key = lambda x: [x[0], -x[1]])
    
    check_g = 0
    count = 0
        
    for i in result_list:
        if check_g == i[0]:
            count += 1
            
            if count > 2:
                continue
            else:
                result.append(i[2])
        else:
            check_g = i[0]
            count = 1
            result.append(i[2])
            
    return result