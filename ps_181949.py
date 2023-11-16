# https://school.programmers.co.kr/learn/courses/30/lessons/181949

str = input()

for i in str:
    if ord(i) > 96:
        print(i.upper(), end='')
    else:
        print(i.lower(), end='')