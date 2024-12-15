# https://school.programmers.co.kr/learn/courses/30/lessons/42839

numbers = "17"
# 3
# numbers = "011"
# # 2

from itertools import permutations
from math import sqrt

def solution(numbers):
    temp_set = set()
    answer = set()
    for i in range(1, len(numbers) + 1):
        for temp in permutations(numbers, i):
            temp_set.add(int("".join(temp)))

    for i in temp_set:
        if i > 1:  # 0과 1은 소수가 아님
            is_prime = True
            for j in range(2, int(sqrt(i)) + 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                answer.add(i)
    return len(answer)



print(solution(numbers))
