from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

q = deque([(0, 0, 1)])

visited = [[0] * M for _ in range(N)]
visited[0][0] = 1

min_dist = 1e9

while q:
    x, y, dist = q.popleft()

    if x == N-1 and y == M-1:
        min_dist = min(min_dist, dist)

    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x+dx, y+dy

        if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1 and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            q.append((nx, ny, dist+1))

print(min_dist)

