# 적록색약
from collections import deque
# bfs 함수 구현
def bfs(x, y, color):
    global n
    visited[y][x] = 1
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and visited[ny][nx] == 0 and color == arr[ny][nx]:
                visited[ny][nx] = 1
                queue.append((nx, ny))

# 입력 받기
n = int(input())
arr = [input() for _ in range(n)]
result1 = 0 # 적록색약이 아닌 사람이 본 구역 수
result2 = 0 # 적록색약인 사람이 본 구역 수
blue_cnt = 0
visited = [[0]*n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 적록색약이 아닌 사람의 경우
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(j, i, arr[i][j])
            result1 += 1
            if arr[i][j] == 'B':
                blue_cnt += 1
for i in range(n):
    arr[i] = arr[i].replace('R', 'G')

visited = [[0]*n for _ in range(n)]
# 적록색약인 사람의 경우
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and arr[i][j] == 'G':
           bfs(j, i, 'G')
           result2 += 1
result2 += blue_cnt

print(result1, result2)