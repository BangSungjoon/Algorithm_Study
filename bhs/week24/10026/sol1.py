from collections import deque
def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            # 배열 범위 내, 색깔 같고, 방문 안한 경우
            if 0 <= nx < N and 0 <= ny < N and graph[x][y] == graph[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = 1  # 방문 처리
                q.append((nx, ny))


N = int(input())
graph = [list(input()) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
answer = [0, 0]
# 비적록색약이 볼 때의 그룹 개수
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            answer[0] += 1
# 적록색약이 볼 때의 그룹 개수를 새기 위하여 초록색을 빨간색으로 바꿈
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'
# 적록색약약이 볼 때의 그룹 개수
visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            answer[1] += 1
# 출력은 gpt 참고
print(' '.join(map(str, answer))) 
