# https://school.programmers.co.kr/learn/courses/30/lessons/87694

rectangle = [[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]]
characterX = 1
characterY = 3
itemX = 7
itemY = 8

# 17

'''
주어진 그래프 좌표대로 하면 탐색을 할 때 버그가 생김
예를 들어 
[F,T,T,F] 
[F,T,T,F] 
이렇게 되어 있고 0,1 -> 0,2 -> 1,2 -> 1,1 이런식으로 가야할 때 
탐색이 어려움
따라서 그래프를 두 배로 늘려준다면 위와 같이 겹치는 부분을 해결할 수 있음
[F,F,T,T,T,T,F,F]
[F,F,F,F,F,T,F,F]
[F,F,F,F,F,T,F,F] 
[F,F,T,T,T,T,F,F]
'''
from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    def bfs(y, x, item_y, item_x, visited, graph):

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        visited[y][x] = True
        cnt = 0
        queue = deque()
        queue.append([y, x, cnt])
        while queue:
            cur_y, cur_x, cnt = queue.popleft()
            if cur_y == item_y and cur_x == item_x:
                # 결과 값은 다시 나누기 2
                return int(cnt // 2)

            for i in range(4):
                next_y = cur_y + dy[i]
                next_x = cur_x + dx[i]

                if graph[next_y][next_x] == 1 and not visited[next_y][next_x]:
                    visited[next_y][next_x] = True
                    queue.append([next_y, next_x, cnt + 1])

    # 그래프 그리기
    def make_graph(data):
        # 2배로 늘려주기
        start_x = data[0] * 2
        start_y = data[1] * 2
        end_x = data[2] * 2
        end_y = data[3] * 2

        for y in range(start_y, end_y + 1):
            for x in range(start_x, end_x + 1):
                # 도형 태두리 안은 다 3으로 표시
                if start_y < y < end_y and start_x < x < end_x:
                    graph[y][x] = 3
                else:
                    # 새로운 도형을 그릴 때 이미 3일 경우 pass
                    if graph[y][x] == 3:
                        continue
                    # 도형의 테두리 부분 1로 채워주기
                    else:
                        graph[y][x] = 1

    # 그래프 2배로 늘려주기
    graph = [[0] * 102 for _ in range(102)]
    visited = [[False] * 102 for _ in range(102)]

    # 그래프 그리기
    for data in rectangle:
        make_graph(data)

    # 캐릭터 좌표와 아이템 좌표도 각각 2배로 그려주기
    return bfs(characterY * 2, characterX * 2, itemY * 2, itemX * 2, visited, graph)


print(solution(rectangle, characterX, characterY, itemX, itemY))
