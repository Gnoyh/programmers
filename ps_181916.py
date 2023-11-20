# https://school.programmers.co.kr/learn/courses/30/lessons/181916

def solution(a, b, c, d):
    check_list = [a, b, c, d]
    count_list = [check_list.count(i) for i in check_list]

    if len(set(check_list)) == 1:
        return 1111 * a
    elif len(set(check_list)) == 2:
        if max(count_list) == 3:
            return (10 * check_list[count_list.index(3)] + check_list[count_list.index(1)]) ** 2
        else:
            return (sum(check_list) // 2) * (abs(sum(check_list) - 4 * a) // 2)
    elif len(set(check_list)) == 3:
        return (sum(check_list) - 2 * check_list[count_list.index(2)] - check_list[count_list.index(1)]) * check_list[
            count_list.index(1)]
    else:
        return min(check_list)