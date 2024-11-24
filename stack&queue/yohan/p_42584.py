# https://school.programmers.co.kr/learn/courses/30/lessons/42584

prices = [1, 2, 3, 2, 3]


# [4, 3, 1, 1, 0]

def solution(prices):
    answer = []
    n = len(prices)
    for i in range(n):
        cnt = 0
        for r in range(i, n - 1):
            if prices[i] <= prices[r+1]:
                cnt += 1
            else:
                cnt += 1
                break
        answer.append(cnt)

    return answer


stack = []
print(solution(prices))
