from collections import deque

T = int(input())

def bfs(i, j):
    q = deque([(i, j)])

    while q:
        x, y = q.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x+dx
            ny = y+dy
            if 0 <= nx < N and 0 <= ny < M and ground[nx][ny] == 1:
                q.append((nx, ny))
                ground[nx][ny] = -1

for t in range(T):
    M, N, K = map(int, input().split())     # 가로, 세로, 배추 위치 개수
    cabbages = [list(map(int, input().split())) for _ in range(K)]

    ground = [[0] * M for _ in range(N)]
    for x, y in cabbages:
        ground[y][x] = 1

    caterpillar = 0

    for i in range(N):
        for j in range(M):
            if ground[i][j] == 1:
                bfs(i, j)
                caterpillar += 1

    print(caterpillar)

