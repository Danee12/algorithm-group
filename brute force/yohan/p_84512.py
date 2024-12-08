# https://school.programmers.co.kr/learn/courses/30/lessons/84512

word = "AAAAE"

def solution(word):
    AEIOU = "AEIOU"
    cnt = 0
    for a in AEIOU:
        temp = a
        cnt += 1
        if temp == word:
            return cnt

        for e in AEIOU:
            temp2 = temp + e
            cnt += 1
            if temp2 == word:
                return cnt

            for i in AEIOU:
                temp3 = temp2 + i
                cnt += 1
                if temp3 == word:
                    return cnt

                for o in AEIOU:
                    temp4 = temp3 + o
                    cnt += 1
                    if temp4 == word:
                        return cnt

                    for u in AEIOU:
                        temp5 = temp4 + u
                        cnt += 1
                        if temp5 == word:
                            return cnt
    return cnt
print(solution(word))