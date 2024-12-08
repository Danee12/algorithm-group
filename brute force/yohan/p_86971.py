# https://school.programmers.co.kr/learn/courses/30/lessons/86971

# n = 4
# wires = [[1, 2], [2, 3], [3, 4]]

# n = 7
# wires = [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]

# n = 9
# wires = [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]

n = 12
wires = [[1, 5], [2, 5], [3, 6], [3, 7], [3, 12], [4, 5], [4, 7], [4, 10], [8, 9], [9, 10], [11, 12]]
# # 답 2


from itertools import combinations
from collections import deque


def solution(n, wires):
    # 두 전력망이 갖게 되는 송전탑의 개수 차이의 절댓값 중 최솟값을 찾기 위해 시작값을 n으로 설정
    answer = n

    def bfs(start):
        visited[start] = True
        queue = deque([start])
        cnt = 1  # 시작 노드를 포함하므로 1로 시작
        while queue:
            cur_v = queue.popleft()
            for v in graph[cur_v]:
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
                    cnt += 1  # 방문할 때마다 1씩 증가
        return cnt

    for c in combinations(wires, len(wires) - 1):
        graph = [[] for _ in range(n + 1)]  # 송전탑 수만큼 그래프 초기화
        visited = [False] * (n + 1)  # 방문 배열 초기화

        # 그래프 구성 (전선 연결)
        for first_node, second_node in c:
            graph[first_node].append(second_node)
            graph[second_node].append(first_node)

        # 송전탑 연결 갯수 계산
        first_network = bfs(1)  # 송전탑은 1번부터 시작한다고 가정

        # 연결이 끊어진 반대편 송전탑 갯수
        second_network = n - first_network

        # 절대값으로 최소값 갱신
        answer = min(answer, abs(first_network - second_network))

    return answer


print(solution(n, wires))
