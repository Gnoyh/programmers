# https://school.programmers.co.kr/learn/courses/30/lessons/178870

def solution(sequence, k):
    result = [-1, -1]

    sum_int = 0
    check_int = len(sequence) - 1

    for i in range(len(sequence) - 1, -1, -1):
        result[1] = i

        if sum_int > 0:
            sum_int -= sequence[i + 1]

        while check_int >= 0:
            sum_int += sequence[check_int]

            if sum_int == k:
                result[0] = check_int

                break
            elif sum_int > k:
                check_int -= 1

                break
            else:
                check_int -= 1

        if result[0] != -1:
            check_index = sequence.index(sequence[result[0]])

            if sequence[result[0]] == sequence[result[1]] and check_index < result[0]:
                return [check_index, check_index + (result[1] - result[0])]
            else:
                return result