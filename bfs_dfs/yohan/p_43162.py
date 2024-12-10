# https://school.programmers.co.kr/learn/courses/30/lessons/43162

# n = 3
# computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

from collections import deque


def solution(n, computers):
    def bfs(start):
        visited[start] = True
        queue = deque([start])
        while queue:
            cur_v = queue.popleft()
            for i in graph[cur_v]:
                if not visited[i]:
                    visited[i] = True
                    queue.append(i)
        return 1

    # 초기 값 셋팅
    graph = {}
    visited = [False] * n
    answer = 0
    for idx, value in enumerate(computers):
        for value_index, v in enumerate(value):
            # 각 컴퓨터들의 연결망을 딕셔너리로 구성
            if idx not in graph and v == 1:
                graph[idx] = [value_index]
            elif v == 1:
                graph[idx].append(value_index)

    # 컴퓨터를 순서대로 돌아줌
    # 각 컴퓨터들이 연결되어 있다면 패스
    # 아닌 경우 bfs를 돌리면서 연결망 체크 및 확인
    for i in range(n):
        if not visited[i]:
            answer += bfs(i)

    return answer


print(solution(n, computers))
