# https://www.acmicpc.net/problem/2579
import sys

input = sys.stdin.readline

n = int(input())

# 계단 값 넣기
stairs = [0] * 301
for i in range(1, n + 1):
    stairs[i] = int(input())

# 메모리 초기화
dp = [0] * 301

# 첫 계단
dp[1] = stairs[1]

# 두 번째 계단
dp[2] = stairs[1] + stairs[2]

# 세 번쨰 계단 (이후로는 연속 3개 밟는 게 안되기 때문에 연산이 동일함)
dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

for i in range(4, n + 1):
    dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])

print(dp[n])
