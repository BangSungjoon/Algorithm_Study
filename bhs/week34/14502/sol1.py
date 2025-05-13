from itertools import combinations
from collections import deque
import copy

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

# 빈 칸과 바이러스 위치 저장
empty = []
virus = []
for y in range(n):
    for x in range(m):
        if lab[y][x] == 0:
            empty.append((y, x))
        elif lab[y][x] == 2:
            virus.append((y, x))

# 상하좌우 방향
directions = [(-1,0), (1,0), (0,-1), (0,1)]

def spread_virus(board):
    q = deque(virus)
    while q:
        y, x = q.popleft()
        for dy, dx in directions:
            ny, nx = y+dy, x+dx
            if 0 <= ny < n and 0 <= nx < m and board[ny][nx] == 0:
                board[ny][nx] = 2
                q.append((ny, nx))
    # 안전 구역 세기
    return sum(row.count(0) for row in board)

max_safe = 0

# 빈 칸 중 3개 고르기
for walls in combinations(empty, 3):
    temp_lab = copy.deepcopy(lab)
    for y, x in walls:
        temp_lab[y][x] = 1  # 벽 세우기
    safe_area = spread_virus(temp_lab)
    max_safe = max(max_safe, safe_area)

print(max_safe)
