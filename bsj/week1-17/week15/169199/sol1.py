from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def solution(board):
    height = len(board)     # 보드의 높이
    width = len(board[0])   # 보드의 넓이

    # 시작지점 R, 목표지점 G 좌표 찾기
    for i in range(height):
        for j in range(width):
            if board[i][j] == 'R':
                sy, sx = i, j
            elif board[i][j] == 'G':
                gy, gx = i, j

    # visited 만들기
    # 이전에 방문한 기록이 있다면 방문 안할 예정
    visited = [[0]*width for _ in range(height)]
    visited[sy][sx] = 1     # 시작지점은 방문하고 시작

    # deque 준비
    queue = deque([(sx, sy, 0)])

    while queue:
        x, y, cnt = queue.popleft()

        # 목표 지점에 도착했다면 함수 종료
        if (x, y) == (gx, gy):
            return cnt

        # 4방향 돌고돌아
        for k in range(4):
            nx, ny = x, y       # nx, ny 초기화
            while True:         # 범위를 벗어나거나 장애물 만날 때까진 달려보는거야...
                nx += dx[k]
                ny += dy[k]
                if not (0 <= nx < width and 0 <= ny < height) or board[ny][nx] == 'D':
                    nx -= dx[k]
                    ny -= dy[k]
                    break
            # 방문한 적이 없다면 방문
            if visited[ny][nx] == 0:
                visited[ny][nx] = 1
                queue.append((nx, ny, cnt+1))
    return -1