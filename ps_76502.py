# https://school.programmers.co.kr/learn/courses/30/lessons/76502

def solution(s):
    p_dict = {"(": 1, ")": -1, "[": 2, "]": -2, "{": 3, "}": -3}

    for i in range(len(s)):
        result = 0
        check = 0

        new_s = s[i: ] + s[: i]
        p_list = []

        for j in new_s:
            if p_dict[j] > 0:
                p_list.append(p_dict[j])
            else:
                if not p_list or abs(p_dict[j]) != p_list[-1]:
                    check = 1

                    break
                else:
                    p_list.pop()

            if p_list == []:
                result += 1

        if check == 0:
            return result

    return 0