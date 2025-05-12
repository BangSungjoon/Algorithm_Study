# [G4] 14502 연구소

import copy
from collections import deque

# STEP 1. 입력 받기
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# STEP 2. 바이러스 전염 함수
def spread():
    q = deque()
    lab = copy.deepcopy(arr)

    for n in range(N):
        for m in range(M):
            if lab[n][m] == 2:      # 이 방이 감염됐다면,
                q.append((n, m))    # 큐에 집어넣기

    while q:
        x, y = q.popleft()
        for dx, dy in [(0, 1), (1, 0), (-1,0), (0, -1)]:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < N and 0 <= ny < M and lab[nx][ny] == 0:    # 범위 안이고, 감염가능한 방이면,
                lab[nx][ny] = 2
                q.append((nx, ny))

    global answer
    cnt = 0

    for row in lab:
        cnt += row.count(0)

    answer = max(answer, cnt)


# STEP 3. 벽 세우는 함수
def add_wall(cnt):
    if cnt == 3:
        spread()
        return

    for n in range(N):
        for m in range(M):
            if arr[n][m] == 0:  # 벽 세우기가 가능하다면,
                arr[n][m] = 1  # 벽을 세우고,
                add_wall(cnt+1) # 두번째 벽을 세우러 간다.
                arr[n][m] = 0  # 백트래킹


answer = 0
add_wall(0)
print(answer)