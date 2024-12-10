# https://school.programmers.co.kr/learn/courses/30/lessons/43165

numbers = [1, 1, 1, 1, 1]
target = 3

from collections import deque


def solution(numbers, target):
    # 초기값 셋팅
    queue = deque()
    queue.append(numbers[0])
    queue.append(numbers[0] * -1)
    queue.append("END")
    cnt = 0

    for i in range(1, len(numbers)):
        # 큐가 한 바퀴 돌 때까지 모든 경우의 수를 큐에 넣어서 관리
        while queue[0] != "END":
            temp = queue.popleft()
            queue.append(temp + numbers[i])
            queue.append(temp - numbers[i])

        # 한 바퀴 다 돌은 큐를 다시 셋팅
        queue.popleft()
        queue.append("END")

    for x in queue:
        # target에 도달한 값들만 카운트
        if x == target:
            cnt += 1

    return cnt


print(solution(numbers, target))
