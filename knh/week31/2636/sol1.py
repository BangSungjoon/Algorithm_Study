from collections import deque

# STEP 1. 입력 받기
r, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]

# STEP 2. 외부 공기아 닿아있는 치즈 판별
def mark_exterior():
    visited = [[False]*c for _ in range(r)]
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True

    while queue:
        x, y = queue.popleft()
        for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                if arr[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                elif arr[nx][ny] == 1:
                    # 외부 공기와 맞닿은 치즈는 2로 마킹
                    arr[nx][ny] = 2
                    visited[nx][ny] = True

# STEP 3. 2로 마킹된 치즈 녹이기
def melt():
    count = 0
    for i in range(r):
        for j in range(c):
            if arr[i][j] == 2:
                arr[i][j] = 0
                count += 1
    return count

time = 0
last = 0

while True:
    mark_exterior()
    melted = melt()
    if melted == 0:
        break
    last = melted
    time += 1

print(time)
print(last)
