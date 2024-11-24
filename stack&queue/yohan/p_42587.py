# https://school.programmers.co.kr/learn/courses/30/lessons/42587

# priorities = [2, 1, 3, 2]
# location = 2
priorities = [1, 1, 9, 1, 1, 1]
location = 0

from collections import deque


def solution(priorities, location):
    queue = deque()
    for idx, value in enumerate(priorities):
        queue.append([value, idx])

    priorities.sort()
    cnt = 0
    while queue:
        if priorities[-1] == queue[0][0]:
            cnt += 1
            priorities.pop()
            temp = queue.popleft()

            if location == temp[1]:
                return cnt
        else:
            queue.append(queue.popleft())


print(solution(priorities, location))
