# https://school.programmers.co.kr/learn/courses/30/lessons/1844

maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]
# 11

from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    visited = [[False] * m for _ in range(n)]

    def bfs(y, x):
        # 처음 시작은 0,0
        visited[y][x] = True
        distance = 1
        queue = deque([[y, x, distance]])
        while queue:
            cur_y, cur_x, distance = queue.popleft()
            # 목표지점에 도달했다면 현재 거리를 리턴해주면서 종료
            if cur_y == n - 1 and cur_x == m - 1:
                return distance
            for i in range(4):
                next_y = cur_y + dy[i]
                next_x = cur_x + dx[i]

                # 전체 그래프안에 있는지 유효성 체크
                if 0 <= next_y < n and 0 <= next_x < m:
                    # 벽인지 체크 및 이전 방문 여부 체크
                    if maps[next_y][next_x] != 0 and not visited[next_y][next_x]:
                        # 새로운 방향으로 나갔다면 distance 값을 올려준 다음 큐에 다시 넣어줌
                        visited[next_y][next_x] = True
                        queue.append([next_y, next_x, distance + 1])

        # 다 돌아도 목적지에 도착하지 못 했다면 -1
        return -1
    return bfs(0, 0)


print(solution(maps))
