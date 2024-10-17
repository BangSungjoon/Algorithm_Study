# 1. 시작 시간이랑 끝 시간 빼서 재생 시간 구하기
def make_play_time(start, end):
    start_h, start_m = map(int, start.split(':'))
    end_h, end_m = map(int, end.split(':'))
    return (end_h * 60 + end_m) - (start_h * 60 + start_m)
# 2. 음 간단하게 처리
def replace_sharp_notes(melody):
     return (melody.replace('C#', 'c')
                  .replace('D#', 'd')
                  .replace('F#', 'f')
                  .replace('G#', 'g')
                  .replace('A#', 'a'))
# 3. 전체 멜로디 생성
def get_full_melody(melody, play_time):
     processed_melody = replace_sharp_notes(melody)
    
    # 재생 시간에 맞게 멜로디 반복 또는 자르기
    if len(processed_melody) >= play_time:
        return processed_melody[:play_time]
    
    # 멜로디 반복
    q, r = divmod(play_time, len(processed_melody))
    return processed_melody * q + processed_melody[:r]

# 4. 처리
def solution(m, musicinfos):
    # 기억한 멜로디에서 #음을 처리
    target = replace_sharp_notes(m)
    
    # 조건을 만족하는 음악을 저장할 리스트
    candidates = []
    
    # 각 음악 정보를 처리
    for i, music in enumerate(musicinfos):
        # 음악 정보 파싱
        start, end, title, melody = music.split(',')
        
        # 재생 시간 계산
        play_time = get_play_time(start, end)
        
        # 실제 재생된 전체 멜로디 생성
        full_melody = get_full_melody(melody, play_time)
        
        # 기억한 멜로디가 재생된 멜로디에 있는지 확인
        if target in full_melody:
            # (재생 시간, 입력 순서, 제목) 형태로 저장
            candidates.append((-play_time, i, title))
    
    # 조건에 맞는 음악이 없는 경우
    if not candidates:
        return "(None)"
    
    # 재생 시간이 긴 순서대로, 같으면 먼저 입력된 순서대로 정렬
    candidates.sort()
    
    # 가장 적합한 음악의 제목 반환
    return candidates[0][2]
    
