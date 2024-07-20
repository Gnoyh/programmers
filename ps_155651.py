# https://school.programmers.co.kr/learn/courses/30/lessons/155651

def solution(book_time):
    result_list = []
    book_time.sort()

    for i, v in enumerate(book_time):
        start_time = v[0].split(":")
        end_time = v[1].split(":")

        book_time[i] = [int(start_time[0]) * 60 + int(start_time[1]), int(end_time[0]) * 60 + int(end_time[1]) + 10]

    for i, v in enumerate(book_time):
        if len(result_list) == 0:
            result_list.append(v[1])
        elif min(result_list) <= v[0]:
            result_list[result_list.index(min(result_list))] = v[1]
        else:
            result_list.append(v[1])

    return len(result_list)