# https://school.programmers.co.kr/learn/courses/30/lessons/12906

arr = [1, 1, 3, 3, 0, 1, 1]


# [1, 3, 0, 1]


def solution(arr):
    list = []
    for i in arr:
        if len(list) == 0:
            list.append(i)
        elif list[-1] == i:
            continue
        else:
            list.append(i)

    return list


print(solution(arr))
