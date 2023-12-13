# https://school.programmers.co.kr/learn/courses/30/lessons/120894

def solution(numbers):
    check_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for i, v in enumerate(check_list):
        if v in numbers:
            numbers = numbers.replace(v, str(i))
            
    return int(numbers)