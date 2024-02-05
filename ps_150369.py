# https://school.programmers.co.kr/learn/courses/30/lessons/150369

def solution(cap, n, deliveries, pickups):
    result = 0

    while deliveries or pickups:
        check_d = check_p = cap
        move_d = 0
        move_p = 0

        while deliveries:
            if deliveries[-1] > 0:
                if move_d == 0:
                    move_d = len(deliveries)

                if deliveries[-1] < check_d:
                    check_d -= deliveries.pop()
                else:
                    deliveries[-1] -= check_d

                    break
            else:
                deliveries.pop()

        while pickups:
            if pickups[-1] > 0:
                if move_p == 0:
                    move_p = len(pickups)

                if pickups[-1] < check_p:
                    check_p -= pickups.pop()
                else:
                    pickups[-1] -= check_p

                    break
            else:
                pickups.pop()

        result += max(move_d, move_p) * 2

    return result