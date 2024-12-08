# https://school.programmers.co.kr/learn/courses/30/lessons/42840

answers = [1, 3, 2, 4, 2]


def solution(answers):
    people_1 = [1, 2, 3, 4, 5]
    people_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    people_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # 각각 PEOPLE_1, PEOPLE_2, PEOPLE_3 의 정답 갯수 초기화
    temp = [0, 0, 0]
    for i in range(len(answers)):
        # 모듈러 연산을 사용해서 수포자가 찍은 답이 시험지의 문제 갯수만큼 알아서 돌아가게 해줌
        if people_1[i % len(people_1)] == answers[i]:
            temp[0] += 1
        if people_2[i % len(people_2)] == answers[i]:
            temp[1] += 1
        if people_3[i % len(people_3)] == answers[i]:
            temp[2] += 1

    target = max(temp)
    answer = []
    for i in range(len(temp)):
        # 각각 사람들의 정답 갯수와 최고 갯수가 같다면 해당 INDEX를 ANSWER에 넣어줌
        if temp[i] == target:
            answer.append(i + 1)

    return answer


print(solution(answers))
