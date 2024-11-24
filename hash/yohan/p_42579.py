# https://school.programmers.co.kr/learn/courses/30/lessons/42579

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 500, 800, 2500]


def solution(genres, plays):
    dic = {}
    n = len(genres)

    # 딕셔너리 작업
    for i in range(n):
        if genres[i] not in dic:
            dic[genres[i]] = [[plays[i], i]]
        else:
            dic[genres[i]].append([plays[i], i])

    # 앞에는 내림차순, 뒤에는 오름차순 ##
    for i, val in dic.items():
        val.sort(reverse=True)
        dic[i] = sorted(val, key=lambda x: (-x[0], x[1]))

    # 장르별 순위 매기기 ##
    from collections import defaultdict

    genre_play_count = defaultdict(int)
    for genre, play in zip(genres, plays):
        genre_play_count[genre] += play

    sorted_genres = sorted(genre_play_count.items(), key=lambda x: x[1], reverse=True)

    sorted_genre_names = [genre for genre, _ in sorted_genres]

    # 정답 추출
    answer = []
    for val in sorted_genre_names:
        if len(dic[val]) > 1:
            answer.append(dic[val][0][1])
            answer.append(dic[val][1][1])
        else:
            answer.append(dic[val][0][1])

    return answer


print(solution(genres, plays))
