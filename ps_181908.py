# https://school.programmers.co.kr/learn/courses/30/lessons/181908

def solution(my_string, is_suffix):
    if len(my_string) < len(is_suffix):
        return 0
    else:
        if is_suffix == my_string[len(my_string) - len(is_suffix): ]:
            return 1
        else:
            return 0