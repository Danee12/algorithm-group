# https://school.programmers.co.kr/learn/courses/30/lessons/42577
def solution(phone_book):
    hash_map = {}
    for nums in phone_book:
        hash_map[nums] = 1

    for nums in phone_book:
        arr = ""
        for num in nums:
            arr += num

            if arr in hash_map and arr != nums:
                return False

    return True


phone_book = ["123", "12", "456"]



print(solution(phone_book))
