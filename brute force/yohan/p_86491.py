# https://school.programmers.co.kr/learn/courses/30/lessons/86491

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]


# 4000

def solution(sizes):
    x = 0
    y = 0
    for i in sizes:
        # max는 명함의 가장 큰 쪽 그 중에 가장 큰 값 찾기
        x = max(x, max(i))
        # min은 명함의 가장 작은 쪽 그 중에 가장 큰 값 찾기
        y = max(y, min(i))

    return x * y


print(solution(sizes))
