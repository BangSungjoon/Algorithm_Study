def solution(m, musicinfos):
    # 기억한 멜로디에서 #이 붙은 음을 소문자로 변환
    m = convert_sharp_notes(m)
    # 결과로 반환할 변수
    answer = None
    # 최대 재생 시간
    max_play_time = 0

    for info in musicinfos:
        # 입력데이터 파싱
        start, end, title, melody = info.split(",")
        # 재생 시간 계산
        play_time = time_to_minute(start, end)
        # 멜로디에서 #이 붙은 음을 소문자로 변환
        melody = convert_sharp_notes(melody)
        
        # 재생된 멜로디 만들기
        # 전체 멜로디 = (원본멜로디 * 반복횟수) + 나머지멜로디
        full_melody = (melody * (play_time // len(melody))) + melody[:play_time % len(melody)]
        
        # 기억한 멜로디 m이 재생된 멜로디에 포함되는지 확인
        if m in full_melody:
            # 조건에 맞는 경우 재생시간이 제일 긴 곡 찾기
            if play_time > max_play_time:
                max_play_time = play_time  # 최대 재생 시간 갱신 후
                answer = title  # 정답 갱신
    # 없으면 None 반환
    return answer if answer else "(None)"


# 재생시간 분단위로 변환하는 함수
def time_to_minute(start, end):
    start_h, start_m = map(int, start.split(":"))
    end_h, end_m = map(int, end.split(":"))
    return (end_h * 60 + end_m) - (start_h * 60 + start_m)

# 악보에서 #이 붙은 음을 소문자로 변환
def convert_sharp_notes(melody):
    melody = melody.replace("C#", "c")
    melody = melody.replace("D#", "d")
    melody = melody.replace("F#", "f")
    melody = melody.replace("G#", "g")
    melody = melody.replace("A#", "a")
    melody = melody.replace("B#", "b")
    return melody

# 결과 출력
print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))