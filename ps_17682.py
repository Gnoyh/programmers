# https://school.programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResult):
    answer = 0

    result = ""
    result_list = []

    bonus_dict = {"S": 1, "D": 2, "T": 3}

    for i in dartResult:
        if i in {"S", "D", "T"}:
            result += i

            result_list.append(result)

            result = ""
        elif i in {"*", "#"}:
            result_list.append(i)
        else:
            result += i

    option = 1
    option_before = 1

    for i in result_list[: : -1]:
        if i == "*":
            option = 2
        elif i == "#":
            option = -1
        else:
            if option_before == 2:
                answer += (int(i[: -1]) ** bonus_dict[i[-1]]) * option * 2

                option_before = option
                option = 1
            else:
                answer += (int(i[: -1]) ** bonus_dict[i[-1]]) * option

                option_before = option
                option = 1

    return answer