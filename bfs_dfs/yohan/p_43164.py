# https://school.programmers.co.kr/learn/courses/30/lessons/43164

# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
# ["ICN", "JFK", "HND", "IAD"]


# tickets = [["ICN", "AAA"], ["ICN", "CCC"], ["CCC", "DDD"], ["AAA", "BBB"], ["AAA", "BBB"], ["DDD", "ICN"],
#            ["BBB", "AAA"]]
# # # 정답 ["ICN", "CCC", "DDD", "ICN", "AAA", "BBB", "AAA", "BBB"]

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]

from collections import deque


def solution(tickets):
    answer = []
    q = deque()
    q.append((["ICN"], []))

    while q:
        # 기록할 경로와 사용한 티켓 기록
        path, used = q.popleft()

        # 사용한 티켓의 수와 전체 티켓의 수가 같다면
        # 모든 티켓을 사용했을 경우 answer에 넣어줌
        if len(used) == len(tickets):
            answer.append(path)

        for idx, ticket in enumerate(tickets):
            depart, arrived = ticket

            # 출발점 유효성확인 및 티켓 사용 여부 확인
            if depart == path[-1] and not idx in used:
                q.append((path + [arrived], used + [idx]))

    # 모든 경로를 순회한 조건의 경로들을 사전순으로 정렬
    answer.sort()

    return answer[0]


print(solution(tickets))
