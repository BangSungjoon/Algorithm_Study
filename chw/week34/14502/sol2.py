from itertools import combinations
from collections import deque
import copy

N, M = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(N)]

def spread(virus_map, wall_idx, virus, cnt):
    q = deque([])
    visited = [[0] * M for _ in range(N)]
    for i, j in wall_idx:
        virus_map[i][j] = 1
        cnt -= 1
    for n, m in virus:
        visited[n][m] = 1
        q.append((n, m))

    while q:
        x, y = q.popleft()
        for dx, dy in (-1,0), (1,0), (0,-1), (0,1):
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < M and virus_map[nx][ny] == 0 and visited[nx][ny] == 0:
                virus_map[nx][ny] = 2
                visited[nx][ny] = 1
                cnt -= 1
                q.append((nx, ny))

    return cnt

space = []      # 벽 설치할 수 있는 위치
virus = []      # 바이러스 위치
cnt = 0         # 안전 영역

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            space.append((i, j))
            cnt += 1
        if arr[i][j] == 2:
            virus.append((i, j))

possible = list(combinations(space, 3))
ans = 0
for wall_idx in possible:
    result = spread(copy.deepcopy(arr), wall_idx, virus, cnt)
    ans = max(ans, result)
print(ans)