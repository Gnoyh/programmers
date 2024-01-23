# https://school.programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    result = []
    
    for i in range(n):
        line = ""
        
        for j in str(bin(arr1[i] | arr2[i]))[2: ]:
            if j == "1":
                line += "#"
            else:
                line += " "
                
        if len(line) < n:
            line = " " * (n - len(line)) + line
                
        result.append(line)
        
    return result