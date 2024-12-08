# https://school.programmers.co.kr/learn/courses/30/lessons/42842

brown = 10
yellow = 2


def solution(brown, yellow):
    for i in range(1, yellow + 1):
        x = i
        y = int(yellow // i)
        # x * y = yellow
        if x * y == yellow:
            # (x+2)(y+2) = brown + xy <- xy 는 yellow 랑 같음
            # 식을 정리하면 아래와 같음
            if (x + y) == int((brown - 4) // 2):
                return [y + 2, x + 2]


print(solution(brown, yellow))
