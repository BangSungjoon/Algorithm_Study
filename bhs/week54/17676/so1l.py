def solution(lines):
    logs = []
    for line in lines:
        date, time, duration = line.split() #자료 공백제거
        h, m, s = time.split(':')
        end_time = (int(h) * 3600 + int(m) * 60 + float(s)) * 1000
        duration = float(duration[:-1]) * 1000
        start_time = end_time - duration + 1
        logs.append((start_time, end_time))
        
    stack = []
    max_output = 0
    
    # 각 로그의 시작 시점을 기준으로 1초 구간 검사
    for i in range(len(logs)):
        start_window = logs[i][0]
        end_window = start_window + 999
        count = 0
        for s, e in logs:
            if e >= start_window and s <= end_window:
                count += 1
        max_output = max(max_output, count)

    # 각 로그의 끝 시점을 기준으로 1초 구간 검사
    for i in range(len(logs)):
        start_window = logs[i][1]
        end_window = start_window + 999
        count = 0
        for s, e in logs:
            if e >= start_window and s <= end_window:
                count += 1
        max_output = max(max_output, count)
            
    return max_output


# 처음에는 시작시간기준으로 스택으로 배열한 후 진행했지만, 히든 케이스 2개가 맞지 않음
# 시작시간과 끝시간 둘 다 살펴보는 완전 탐색으로 구간 검사를 진행하니까 통과