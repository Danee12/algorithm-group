# https://school.programmers.co.kr/learn/courses/30/lessons/1845

nums = [3, 1, 2, 3]


# 2

# nums = [3, 3, 3, 2, 2, 4]
# # 3
#
# nums = [3, 3, 3, 2, 2, 2]
# # 2

def solution(nums):
    nums_set = set(nums)
    n = int(len(nums) / 2)
    if len(nums_set) == n:
        return n
    elif len(nums_set) < n:
        return len(nums_set)
    else:
        return n

def solution(nums):
    answer = 0
    return answer

print(solution(nums))