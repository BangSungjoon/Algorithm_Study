# 방금그곡, 17683
def solution(m, musicinfos):
    answer = '(None)'
    max_time = 0
    for musicinfo in musicinfos:
        music = musicinfo.split(',')
        hour = int(music[1][:2]) - int(music[0][:2])
        minute = int(music[1][3:]) - int(music[0][3:])
        time = 60*hour + minute
        cnt = 0             # 재생 시간
        i = 0               # 악보 idx
        real_music = ''     # 방송된 음악

        # 재생 시간 동안 재생
        while cnt < time:
            if i >= len(music[3]):
                i = 0
            real_music += music[3][i]
            i += 1
            # 다음꺼 # 이면 하나 더 넣어
            if i < len(music[3]) and music[3][i] == '#':
                real_music += music[3][i]
                i += 1
            # 시간이 흐른다....
            cnt += 1
            # 내가 기억하는 멜로디 길이보다 길어졌다면 검사한당
            if len(real_music) >= len(m):
                if m == real_music[len(real_music)-len(m):]:
                    if answer == '(None)':  # 맞는게 처음이라면
                        answer = music[2]
                        max_time = time
                    else:                   # 너 처음이 아니구나?
                        if time > max_time: # 재생시간 더 길면 인정
                            answer = music[2]
                            max_time = time

    return answer