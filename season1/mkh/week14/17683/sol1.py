def solution(m, musicinfos):
    n_m = m.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a').replace('B#','b')
    # #이 붙은 코드들을 하나의 글자로 인식하기 위해 소문자로 치환
    ls =[]
    # 정답의 가능성이 있는 노래들을 담을 ls
    for i in range(len(musicinfos)):
        musicinfo = musicinfos[i].replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a').replace('B#','b').split(',')
        # 소문자로 치환한 글자들을 , 로 split해서 리스트로 만듦.
        # ['12:00', '12:14', 'HELLO', 'CDEFGAB'], ['13:00', '13:05', 'WORLD', 'ABCDEF']
        lastingtime = int(musicinfo[1][:2])*60+int(musicinfo[1][3:]) - int(musicinfo[0][:2])*60-int(musicinfo[0][3:])
        # (종료시간의 시 * 60 + 분) - (시작시간의 시 * 60 + 분) = 지속시간
        notes = musicinfo[3] * (lastingtime//len(musicinfo[3])) + musicinfo[3][:lastingtime%len(musicinfo[3])]
        # 노래의 재생시간 동안 어떤 노트들이 재생되었는지 담는 notes
        if n_m in notes:
            # n_m이 note에 있다면
            ls.append((lastingtime, i, musicinfo[2]))
            # 지속시간, 순서, 제목으로 리스트를 담는다.
    ls.sort(key=lambda x:(x[0], -x[1]), reverse=True)
    # 지속시간이 긴 순서, 그 다음에는 순서가 빠른 순서로 정렬한다.
    if ls:
        return ls[0][2]
    # 정답이 있다면 0번째 원소의 2번째 원소 제목을 리턴한다.    
    else:
        return '(None)'
