def solution(genres, plays):
    genre_dict = dict()

    # 1. 장르 dict에 플레이 횟수 저장
    for i in range(len(genres)):
        if genres[i] not in genre_dict.keys():
            genre_dict[genres[i]] = [plays[i], [(i, plays[i])]]
        else:
            value = genre_dict[genres[i]]
            value[0] += plays[i]
            value[1].append((i, plays[i]))
            genre_dict[genres[i]] = value

    # 2. 장르별 총 횟수 내림차순 정렬
    genre_plays = list(genre_dict.values())
    genre_plays.sort(key=lambda x: -x[0])

    # 3. 각 장르별 노래 2개씩 answer에 추가
    answer = []
    for genre in genre_plays:
        play_list = sorted(genre[1], key=lambda x: (-x[1], x[0]))
        for p in play_list[:2]:     # 이러면 1개만 있어도 1개만 잘라옴
            answer.append(p[0])
    print(answer)
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
solution(genres, plays)