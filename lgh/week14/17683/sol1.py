# 방금그곡
# m 네오가 기억한 멜로디, musicinfos(시작시간, 끝난시간, 제목, 악보)
# 음은 1분에 1개씩
# 여러개일때는 재생시간 가장 긴 음악 제목 반환
# 재생시간같을때는 먼저 입력된 음악 반환

# '#'붙은 음표를 소문자로 변환
def shap_to_lower(s):  
    s = s.replace('C#', 'c')
    s = s.replace('D#', 'd')
    s = s.replace('F#', 'f')
    s = s.replace('G#', 'g')
    s = s.replace('A#', 'a')
    s = s.replace('B#', 'b') # 문제에 없지만 b#추가하기(테케34번)
    return s

def solution(m, musicinfos):
    data = []  # 음악 정보를 저장할 리스트 (재생시간, 제목, 악보정보)
    m = shap_to_lower(m)  # 입력된 멜로디를 소문자로 변환
    answer = '(None)'  # 초깃값은 None으로 설정
    max_time = 0  # 가장 긴 재생 시간을 저장할 변수

    for info in musicinfos: # 예시 ['13:00,13:05,WORLD,ABCDEF']
        start, end, title, melody = info.split(',')  # ('13:00', '13:05', 'WORLD', 'ABCDEF')
        start_h, start_m = map(int, start.split(':')) # 시작시간 
        end_h, end_m = map(int, end.split(':')) # 끝난 시간
        time = (end_h * 60 + end_m) - (start_h * 60 + start_m) # 재생시간(분 단위)

        melody = shap_to_lower(melody) # 주어진 악보 변환
       
        full_melody = (melody * (time // len(melody) + 1))[:time]  # melody를 (재생시간을 멜로디로 나눈 몫 + 1)번 반복후 원래 내 재생시간 만큼만 뽑음

        if m in full_melody: # 네오가 기억한 멜로디가 악보에 있을 경우
            if time > max_time: # 재생시간이 제일 긴 음악 제목 반환
                max_time = time
                answer = title
     
    return answer

print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
