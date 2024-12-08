# https://school.programmers.co.kr/learn/courses/30/lessons/87946

dungeons = [[80, 20], [50, 40], [30, 10]]
k = 80

from itertools import permutations

# 순서가 필요하니깐 순열
def solution(k, dungeons):
    max_cnt = 0
    for i in permutations(dungeons, len(dungeons)):
        # k 와 cnt 초기화
        start = k
        cnt = 0

        # 모든 경우의 수를 게산하면서 조건에 만족하지 않으면 break
        for requisite, energy in i:
            if start >= requisite:
                start -= energy
                cnt += 1
            else:
                break
        # 반복문이 끝난후 현재 카운팅 된 수와 max 값을 갱신
        max_cnt = max(max_cnt, cnt)
    return max_cnt


print(solution(k, dungeons))
