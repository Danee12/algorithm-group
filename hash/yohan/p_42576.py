# https://school.programmers.co.kr/learn/courses/30/lessons/42576?language=python3

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]


# leo


def solution(participant, completion):
    participant.sort()
    completion.sort()
    n = len(participant)
    for i in range(n - 1):
        if completion[i] != participant[i]:
            return participant[i]

    return participant[n - 1]


print(solution(participant, completion))
