# https://school.programmers.co.kr/learn/courses/30/lessons/42747

citations = [3, 0, 6, 1, 5]
# 3
# citations = [3, 4]
# # 2


def solution(citations):
    citations.sort(reverse=True)
    temp = []
    for i in citations:
        if i == 0:
            break
        temp.append(i)

    temp.sort()
    answer = 0
    cnt = 0

    for i in range(1, len(temp)+1):
        for r in temp:
            if i <= r:
                cnt += 1
        n = i
        if n <= cnt and answer < n:
            answer = n
        else:
            break
        print(f"{i}번째 {cnt}번")
        cnt = 0
    return answer

# citations = [3, 0, 6, 1, 5]
# def solution(citations):
#     citations.sort(reverse=True)
#     rank_citations = enumerate(citations, start=1)
#     x = map(min, rank_citations)
#     answer = max(x)
#     return answer

print(solution(citations))
