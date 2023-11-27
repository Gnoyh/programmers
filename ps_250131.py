# https://school.programmers.co.kr/learn/courses/30/lessons/250131

year = int(input())
age_type = input()

if age_type == "Korea":
    answer = 2030 - year + 1
else:
    answer = 2030 - year

print(answer)