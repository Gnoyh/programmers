# https://school.programmers.co.kr/learn/courses/30/lessons/77885

def solution(numbers):
    result = []
    
    for i in numbers:
        check_bin = "0" + bin(i)[2: ]
        
        if i % 2 == 0:
            result.append(i + 1)
        else:
            for j, v in enumerate(check_bin[: : -1]):
                if v == "0":
                    result.append(i + 2 ** (j - 1))
                    
                    break
                    
    return result