# https://school.programmers.co.kr/learn/courses/30/lessons/42578
# https://dduniverse.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%9D%98%EC%83%81-%ED%8C%8C%EC%9D%B4%EC%8D%AC-python
clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]


# 5
# clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
# # 3

def solution(clothes):
    dic = {}
    for i in clothes:
        if i[1] in dic:
            dic[i[1]].append(i[0])
        else:
            dic[i[1]] = [i[0]]

    answer = 1
    for _, value in dic.items():
        answer *= (len(value) + 1)

    return answer-1

print(solution(clothes))
