# 프로그래머스 250136 석유 시추 문제
# 우선도 아래, 오른쪽, 왼쪽, 위
# 정답은 다 맞으나 효율성테스트 실패
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def solution(land):
    # 세로 n, 가로 m
    n, m = len(land), len(land[0])

    # land가 0이면 빈 땅, 1이면 석유
    # x좌표 기준 석유 매장량을 기록할 배열
    oil = [0]*m

    # visited
    visited = [[0]*m for _ in range(n)]

    # dfs
    def dfs(x, y):
        nonlocal n, m, size

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < m and 0 <= ny < n and land[ny][nx] == 1 and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                size += 1
                x_oil.add(nx)
                dfs(nx, ny)

    # 탐사
    for i in range(n):
        for j in range(m):
            # 만약 석유를 만났다면
            if land[i][j] == 1 and visited[i][j] == 0:
                size = 1
                x_oil = set()
                x_oil.add(j)
                visited[i][j] = 1
                dfs(j, i)
                for x in x_oil:
                    oil[x] += size

    return max(oil)