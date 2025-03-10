# 토마토
from collections import deque

col, row = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(row)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0

q = deque()
for i in range(row):
    for j in range(col):
        if arr[i][j] == 1:
            # y, x 값 저장
            q.append([i, j, 0])

# bfs 시작
while q:
    y, x, cnt = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= ny < row and 0 <= nx < col and arr[ny][nx] == 0:
            arr[ny][nx] = 1
            q.append([ny, nx, cnt+1])
# 전부 익었는지 검사하기
for i in range(row):
    for j in range(col):
        if arr[i][j] == 0:
            cnt = -1

print(cnt)