# https://school.programmers.co.kr/learn/courses/30/lessons/150370

def solution(today, terms, privacies):
    result = []
    terms_list = {}
    lastday_list = []

    for i in terms:
        term = i.split()

        terms_list[term[0]] = int(term[1])

    for i in privacies:
        privacy = i.split()
        date = list(map(int, privacy[0].split(".")))

        lastday_list.append(date[0] * 12 * 28 + (date[1] + terms_list[privacy[1]]) * 28 + date[2] - 1)

    today_list = list(map(int, today.split(".")))

    today = today_list[0] * 12 * 28 + today_list[1] * 28 + today_list[2]

    for i in range(len(lastday_list)):
        if lastday_list[i] < today:
            result.append(i + 1)

    return result