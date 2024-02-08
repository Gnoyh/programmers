# https://school.programmers.co.kr/learn/courses/30/lessons/132265

def solution(topping):
    result = 0

    left_list = []
    right_list = []

    topping_set = set()

    for i in topping:
        if not i in topping_set:
            topping_set.add(i)

        left_list.append(len(topping_set))

    topping_set = set()

    for i in topping[: : -1]:
        if not i in topping_set:
            topping_set.add(i)

        right_list.append(len(topping_set))

    right_list = right_list[: : -1]

    idx = 0

    while 0 <= idx < len(topping) - 1:
        if left_list[idx] < right_list[idx + 1]:
            idx += 1
        elif left_list[idx] == right_list[idx + 1]:
            result += 1
            idx += 1
        else:
            break

    return result