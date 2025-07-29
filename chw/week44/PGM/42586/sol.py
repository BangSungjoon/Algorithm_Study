from collections import deque

def solution(progresses, speeds):
    answer = []
    days = deque()

    # 각 기능 배포까지 걸리는 날짜 계산
    for progress, speed in zip(progresses, speeds):
        remain = (100 - progress + speed - 1) // speed  # 올림 처리
        days.append(remain)

    while days:
        cnt = 1
        current = days.popleft()

        # 현재 기능과 함께 배포 가능한 기능 세기
        while days and days[0] <= current:
            days.popleft()
            cnt += 1

        answer.append(cnt)

    return answer