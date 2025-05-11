from itertools import combinations
from collections import deque
import copy

N, M = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(N)]

def spread(virus_map, wall_idx):
    q = deque([])
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if (i, j) in wall_idx:
                virus_map[i][j] = 1
            if virus_map[i][j] == 2:
                visited[i][j] = 1
                q.append((i, j))
    while q:
        x, y = q.popleft()
        for dx, dy in (-1,0), (1,0), (0,-1), (0,1):
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < M and virus_map[nx][ny] == 0 and visited[nx][ny] == 0:
                virus_map[nx][ny] = 2
                visited[nx][ny] = 1
                q.append((nx, ny))

    # 안전 영역 계산
    cnt = 0
    for n in range(N):
        for m in range(M):
            if virus_map[n][m] == 0:
                cnt += 1
    return cnt

space = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            space.append((i, j))

possible = list(combinations(space, 3))
ans = 0
for wall_idx in possible:
    result = spread(copy.deepcopy(arr), wall_idx)
    ans = max(ans, result)
print(ans)