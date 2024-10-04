import sys
from collections import deque
sys.stdin = open('C:\\dev\\Algorithm\\1249\\input.txt')

def BFS(start, end):
    queue = deque([start])  # start 좌표 큐에 넣고 시작
    min_time = [[float('inf')]*N for _ in range(N)]  # 최소 시간 기록해야하니까 무한대로 초기화
    min_time[start[0]][start[1]] = 0  # 시작점의 최소 시간을 0으로 설정 (시작점에서 시작하니까 시간: 0)

    # 큐가 비기 전까지 반복
    while queue:
        x, y = queue.popleft()  # 큐의 맨 앞 꺼냄
        # 델타 탐색
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy  # 새로운 좌표 계산
            # 범위 확인
            if 0 <= nx < N and 0 <= ny < N:
                # 새로운 좌표로 이동할 때 걸리는 시간 계산
                new_time = min_time[x][y] + arr[nx][ny]
                # 최소값 갱신
                if new_time < min_time[nx][ny]:
                    min_time[nx][ny] = new_time
                    queue.append((nx, ny))  # 새로 갱신된 좌표를 큐에 추가해서 탐색 계속
    return min_time[end[0]][end[1]]


T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 지도 크기
    arr = [list(map(int, input())) for _ in range(N)]
    # print(N)
    # print(arr)
    sx, sy = 0, 0  # 시작 좌표
    ex, ey = N-1, N-1  # 도착 좌표

    # BFS 수행하며 최소 복구 시간 계산 후 출력
    print(f'#{tc} {BFS((sx,sy), (ex, ey))}')