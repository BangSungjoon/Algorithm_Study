def solution(genres, plays):
    answer = []
    
    # STEP 1. 음악을 전부 합치기
    musics = {}
    
    for i in range(len(genres)):
        key = genres[i]
        
        if key in musics:
            musics[key].append((i, plays[i]))
        else:
            musics[key] = [(i, plays[i])]
    
    # STEP 2. 베스트 앨범 만들기
    genres_sorted = []
    for key in musics.keys():
        genres_sorted.append((key, sum([x[1] for x in musics[key]])))
    genres_sorted = sorted(genres_sorted, key = lambda x: -x[1])
    
    for key, _ in genres_sorted:
        album = sorted(musics[key], key = lambda x: -x[1])
        
        for item in album[:2]:
            answer.append(item[0])
    return answer
