# https://school.programmers.co.kr/learn/courses/30/lessons/42748

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array, commands):
    answer = []
    for start, end, target in commands:
        temp = sorted(array[start-1:end])
        answer.append(temp[target-1])
    return answer

print(solution(array, commands))