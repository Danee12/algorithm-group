# https://school.programmers.co.kr/learn/courses/30/lessons/43163

# begin = "hit"
# target = "cog"
# words = ["hot", "dot", "dog", "lot", "log", "cog"]
#

begin = "aab"
target = "aba"
words = ["abb", "aba"]
# # 2

# begin = "hit"
# target = "hhh"
# words = ["hhh", "hht"]
# 2

from collections import deque


def solution(begin, target, words):
    # words에 처음부터 단어가 없을 경우 0 리턴
    if target not in words:
        return 0

    # 전체 노드 갯수
    n = len(words)

    # 방문 노드 기록
    visited = [False] * n

    queue = deque([[begin, 0]])

    while queue:
        temp, cnt = queue.popleft()
        if temp == target:
            return cnt

        for i in range(n):
            # 방문한 적이 없을 경우 실행
            if not visited[i]:
                difference = 0

                # 현재의 단어가 바꿀 단어랑 몇 글자가 다른지 체크
                for r in range(len(words[i])):
                    if temp[r] != words[i][r]:
                        difference += 1

                # 1개만 다를 경우 바꿀 수 있으므로 1개만 다르면 바꿔줌
                if difference == 1:
                    next = words[i]

                    # 바꾼 단어의 노드를 True 체크 -> 재방문 방지
                    visited[i] = True

                    # 방문횟수 카운팅 추가
                    queue.append([next, cnt + 1])


print(solution(begin, target, words))
