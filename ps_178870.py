# https://school.programmers.co.kr/learn/courses/30/lessons/178870

def solution(sequence, k):
    result = [0, len(sequence)]

    if k in sequence:
        return [sequence.index(k), sequence.index(k)]

    for i in range(len(sequence)):
        check_sum = sequence[i]

        check_list = [i]

        for j in range(i + 1, len(sequence)):
            check_sum += sequence[j]

            if check_sum == k:
                check_list.append(j)

                break
            elif check_sum > k:
                break

        if len(check_list) == 2:
            if check_list[1] - check_list[0] < result[1] - result[0]:
                result = check_list.copy()

    return result