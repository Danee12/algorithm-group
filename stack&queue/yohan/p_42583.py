# https://school.programmers.co.kr/learn/courses/30/lessons/42583

bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]

from collections import deque


def solution(bridge_length, weight, truck_weights):
    bridge_q = deque([0] * bridge_length)
    truck_q = deque(truck_weights)
    current_weight = 0
    time_cnt = 0

    while bridge_q:
        current_weight -= bridge_q.popleft()
        time_cnt += 1

        if truck_q:
            if weight >= current_weight + truck_q[0]:
                truck = truck_q.popleft()
                current_weight += truck
                bridge_q.append(truck)

            else:
                bridge_q.append(0)

    return time_cnt


print(solution(bridge_length, weight, truck_weights))
