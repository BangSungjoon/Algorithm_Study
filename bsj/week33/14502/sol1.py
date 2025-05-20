from itertools import combinations
from collections import deque
# 1. 입력 처리
n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

# 빈 칸과 바이러스 위치 수집
빈칸 = []
바이러스 = []
for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            빈칸.append((i, j))
        if lab[i][j] == 2:
            바이러스.append((i, j))

# 상하좌우 방향 벡터
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

result = 0  # 안전 영역 최대값

# 2. 벽 3개 설치 조합 생성
for walls in combinations(빈칸, 3):
    # 3. 원본 맵 깊은 복사 및 벽 세우기
    tmp = [row[:] for row in lab]
    for x, y in walls:
        tmp[x][y] = 1

    # 바이러스 퍼뜨리기 BFS
    queue = deque(바이러스)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                queue.append((nx, ny))

    # 4. 안전 영역 개수 세기
    safe_count = sum(row.count(0) for row in tmp)
    result = max(result, safe_count)

# 5. 결과 출력
print(result)
