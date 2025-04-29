N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
res = 0

# 상하좌우 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, depth, total):
    global res
    # 4칸을 모두 선택했으면 최대값 갱신
    if depth == 4:
        res = max(res, total)
        return
    for vec in range(4):
        nx, ny = x + dx[vec], y + dy[vec]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, depth + 1, total + board[nx][ny])
            visited[nx][ny] = False

def check_fuck(x, y):
    global res
    # ㅗ 모양만 별도로 처리: 중심 칸 + 그 주변 4칸 중 값이 큰 3개 합
    wing_values = []
    for vec in range(4):
        nx, ny = x + dx[vec], y + dy[vec]
        if 0 <= nx < N and 0 <= ny < M:
            wing_values.append(board[nx][ny])
    if len(wing_values) >= 3:
        total = board[x][y] + sum(sorted(wing_values, reverse=True)[:3])
        res = max(res, total)

for i in range(N):
    for j in range(M):
        # DFS로 I, O, L, J, S, Z 모양 처리
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False
        # ㅗ 모양 처리
        check_fuck(i, j)

print(res)
