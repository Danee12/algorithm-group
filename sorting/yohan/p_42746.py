# https://school.programmers.co.kr/learn/courses/30/lessons/42746

# numbers = [6, 10, 2]
# # "6210"

numbers = [3, 30, 34, 5, 9]
# "9534330"


def solution(numbers):
    temp = []
    for i in numbers:
        temp.append(str(i))
    temp.sort(key=lambda x: x*3, reverse=True)

    answer = ''
    for i in temp:
        answer += i
    return answer

print(solution(numbers))