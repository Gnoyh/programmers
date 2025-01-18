# https://school.programmers.co.kr/learn/courses/30/lessons/17686

def solution(files):
    num = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    new_files = []
    
    for i, v in enumerate(files):
        new_file = []
        start_idx = 0
        
        for j, w in enumerate(v):
            if w in num and len(new_file) == 0:
                start_idx = j
                
                new_file.append(v[: j])
            elif w not in num and len(new_file) == 1:
                new_file.append(v[start_idx: j])
                
                break
                
        if len(new_file) == 1:
            new_file.append(v[start_idx: ])
                
        new_file.append(i)
        new_files.append(new_file)
        
    new_files.sort(key = lambda x : (x[0].upper(), int(x[1][: 5])))
    
    result = []
    
    for i in new_files:
        result.append(files[i[2]])
        
    return result