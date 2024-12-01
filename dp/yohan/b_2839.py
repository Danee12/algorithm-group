# https://www.acmicpc.net/problem/2839

n = int(input())
cnt = 0

# n이 다 없어질 때까지 돎 -> 안 끝나면 답이 없는 것이므로 -1
while n >= 0:
    # 5로 나눠진다면 바로 나눈 값의 몫을 합쳐서 리턴
    if n % 5 == 0:
        cnt += n // 5
        print(cnt)
        break
    # 5로 나눠지지 않는다면 -3 을 하고 3kg을 포장 했으니 포장 수량을 1개 올려준다
    else:
        n -= 3
        cnt += 1
else:
    print(-1)
