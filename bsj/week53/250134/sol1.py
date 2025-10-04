def solution(maze):
    n = len(maze)
    m = len(maze[0])
    r, b, r_g, b_g = None, None, None, None
    wall = set()
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1:       # 빨간 수레 시작
                r = (i, j)
            elif maze[i][j] == 2:     # 파란 수레 시작
                b = (i, j)
            elif maze[i][j] == 3:     # 빨간 수레 도착
                r_g = (i, j)
            elif maze[i][j] == 4:     # 파란 수레 도착
                b_g = (i, j)
            elif maze[i][j] == 5:     # 벽
                wall.add((i, j))
                
    visited_r = [[0]*m for _ in range(n)]
    visited_b = [[0]*m for _ in range(n)]
    visited_r[r[0]][r[1]] = 1
    visited_b[b[0]][b[1]] = 1

    answer = float('inf')

    def next(x, y, goal, visited):
        if (x, y) == goal:
            return [(x, y, 0)]  # 도착 시 이동하지 않음
        result = []
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if (nx, ny) in wall:
                continue
            if visited[nx][ny] == 1:
                continue
            result.append((nx, ny, 1))   # (좌표, 방문표시여부=1)
        return result

    def dfs(rx, ry, bx, by, turn):
        nonlocal answer
        if turn >= answer:
            return
        if (rx, ry) == r_g and (bx, by) == b_g:
            answer = min(answer, turn)
            return

        r_moves = next(rx, ry, r_g, visited_r)
        b_moves = next(bx, by, b_g, visited_b)

        for nrx, nry, r_arrive in r_moves:
            # r_arrive: 빨간 수레가 새 칸을 밟았는가?
            for nbx, nby, b_arrive in b_moves:
                # 규칙 위반 처리
                if (nrx, nry) == (nbx, nby):  # 같은 칸 동시 진입 안됨
                    continue
                if (nrx, nry) == (bx, by) and (nbx, nby) == (rx, ry):  # 자리바꿈은 안됨
                    continue

                if r_arrive:  # 다음 칸으로 이동한거임? ㅇㅇ 방문처리 하쇼
                    visited_r[nrx][nry] = 1
                if b_arrive:
                    visited_b[nbx][nby] = 1

                dfs(nrx, nry, nbx, nby, turn + 1)

                if r_arrive:  # 방문처리 했던거 취소
                    visited_r[nrx][nry] = 0
                if b_arrive:
                    visited_b[nbx][nby] = 0

    dfs(r[0], r[1], b[0], b[1], 0)
    return 0 if answer == float('inf') else answer