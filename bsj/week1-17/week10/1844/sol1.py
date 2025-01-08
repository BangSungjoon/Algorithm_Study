# programmers 게임 맵 최단거리

# 방향 벡터
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def solution(maps):
    answer = float('inf')   # 최솟값을 찾을거니깐 일단 겁나 크게 만들기
    # 세로 길이 n
    n = len(maps)
    # 가로 길이 m
    m = len(maps[0])

    # visited 만들기
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1   # 출발지점 방문
    # dfs
    def dfs(y, x, cnt):
        nonlocal answer     # 중첩 함수에서 상위 변수를 수정할 수 있게 선언
        # 백트래킹
        if cnt < answer:
            # 기저 조건
            if y == n-1 and x == m-1:
                answer = cnt
                return
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == 0 and maps[ny][nx] == 1:
                    visited[ny][nx] = 1
                    dfs(ny, nx, cnt+1)
                    visited[ny][nx] = 0
    dfs(0, 0, 1)
    if answer == float('inf'):
        answer = -1

    return answer