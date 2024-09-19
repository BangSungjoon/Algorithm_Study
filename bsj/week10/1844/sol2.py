# programmers 게임 맵 최단거리
from collections import deque
# 방향 벡터
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def solution(maps):
    # 세로 길이 n
    n = len(maps)
    # 가로 길이 m
    m = len(maps[0])

    # visited 만들기
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1   # 출발지점 방문

    queue = deque([(0, 0, 1)])

    while queue:
        y, x, cnt = queue.popleft()

        # 목적지에 도달한 경우
        if y == n-1 and x == m-1:
            return cnt
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == 0 and maps[ny][nx] == 1:
                visited[ny][nx] = 1
                queue.append((ny, nx, cnt+1))

    return -1