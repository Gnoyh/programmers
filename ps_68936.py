# https://school.programmers.co.kr/learn/courses/30/lessons/68936

def solution(arr):
    result = [0, 0]

    def compressor(start_x, end_x, start_y, end_y, len_arr):
        check_sum = sum([sum(arr[i][start_x: end_x]) for i in range(start_y, end_y)])

        if check_sum == 0:
            result[0] += 1
        elif check_sum == len_arr ** 2:
            result[1] += 1
        elif len_arr == 2:
            result[0] += 4 - check_sum
            result[1] += check_sum
        else:
            compressor(start_x, (start_x + end_x) // 2, start_y, (start_y + end_y) // 2, len_arr // 2)
            compressor((start_x + end_x) // 2, end_x, start_y, (start_y + end_y) // 2, len_arr // 2)
            compressor(start_x, (start_x + end_x) // 2, (start_y + end_y) // 2, end_y, len_arr // 2)
            compressor((start_x + end_x) // 2, end_x, (start_y + end_y) // 2, end_y, len_arr // 2)

    compressor(0, len(arr), 0, len(arr), len(arr))

    return result