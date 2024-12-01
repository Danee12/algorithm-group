# https://school.programmers.co.kr/learn/courses/30/lessons/43105

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]


def solution(triangle):
    memory = [0]
    for i in range(len(triangle)):
        temp = [0] * (i + 1)
        last_idx = i
        for j in range(i + 1):
            # 인덱스 처음 부분일 때
            if j == 0:
                temp[0] = memory[0] + triangle[i][j]
            # 인덱스 마지막 부분일 때
            elif j == last_idx:
                temp[-1] = memory[-1] + triangle[i][j]
            # 그 외는 앞 뒤 계산해서 max 값에 넣어줌
            else:
                temp[j] += max(memory[j - 1] + triangle[i][j], memory[j] + triangle[i][j])

        # 메모리 업데이트
        memory = [i for i in temp]

    return max(memory)

    # for i in range(1, len(triangle)):
    #     for _ in range(len(target)):
    #         z = target.popleft()
    #         for j in range(len(triangle[i])-1):
    #             for r in range(0+j, 1+j):
    #                 target.append(z + triangle[i][r])


print(solution(triangle))
