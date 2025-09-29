from collections import deque

T = int(input())

for t in range(T):
    w, h = map(int, input().split())
    building = [list(input()) for _ in range(h)]

    q = deque([])
    fire = deque([])

    # 상근이랑 불 찾기
    for i in range(h):
        for j in range(w):
            if building[i][j] == '@':
                q.append((i, j, 0))

            if building[i][j] == '*':
                fire.append((i, j))

    visited = [[0] * w for _ in range(h)]

    min_move = 1e9

    # 매 초 상근이랑 불 움직임
    while q:
        # 불 번짐
        for _ in range(len(fire)):
            k, s = fire.popleft()

            for dk, ds in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nk, ns = k+dk, s+ds
                if 0 <= nk < h and 0 <= ns < w and building[nk][ns] in ['.', '@']:
                    fire.append((nk, ns))
                    building[nk][ns] = '*'

        # 상근이 움직임
        for _ in range(len(q)):
            x, y, cnt = q.popleft()

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < h and 0 <= ny < w:
                    if visited[nx][ny] == 0 and building[nx][ny] == '.':
                        q.append((nx, ny, cnt+1))
                        visited[nx][ny] = 1
                else:
                    min_move = min(min_move, cnt+1)

    if min_move == 1e9:
        print('IMPOSSIBLE')
    else:
        print(min_move)