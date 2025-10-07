from collections import deque

def solution(maze):
    n = len(maze)
    m = len(maze[0])

    ri, rj = 0, 0
    bi, bj = 0, 0

    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1:
                ri, rj = i, j

            if maze[i][j] == 2:
                bi, bj = i, j

    r_visited = {(ri, rj)}
    b_visited = {(bi, bj)}

    q = deque([(ri, rj, bi, bj, 0, r_visited, b_visited)])

    while q:
        rx, ry, bx, by, cnt, rv, bv = q.popleft()

        # 둘 다 도착
        if maze[rx][ry] == 3 and maze[bx][by] == 4:
            return cnt

        # 1. 빨간 수레의 움직임 후보 리스트 생성
        red_moves = []
        if maze[rx][ry] == 3:
            red_moves.append((rx, ry))
        else:
            for drx, dry in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                red_moves.append((rx + drx, ry + dry))  # 아니면 4방향 추가

        # 2. 파란 수레의 움직임 후보 리스트 생성 (빨강과 동일한 로직)
        blue_moves = []
        if maze[bx][by] == 4:
            blue_moves.append((bx, by))
        else:
            for dbx, dby in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                blue_moves.append((bx + dbx, by + dby))  # 아니면 4방향 추가

        # 3. 두 리스트를 조합하여 모든 경우의 수 생성
        for nrx, nry in red_moves:
            for nbx, nby in blue_moves:

                # 퍼즐 안에 있는지
                if 0 <= nrx < n and 0 <= nry < m and 0 <= nbx < n and 0 <= nby < m:

                    # 벽이 아닌지
                    if maze[nrx][nry] != 5 and maze[nbx][nby] != 5:

                        # 두 수레가 같은 곳이 아닌지
                        if (nrx, nry) != (nbx, nby):

                            # 서로 자리를 바꾼 건 아닌지
                            if not ((nrx, nry) == (bx, by) and (nbx, nby) == (rx, ry)):

                                # 방문한 적 없는 곳인지
                                if (nrx, nry) not in rv and (nbx, nby) not in bv:
                                    n_rv = rv.copy()
                                    n_bv = rv.copy()

                                    # 다음 갈 곳이 도착지라면 방문 처리하지 말기
                                    if maze[nrx][nry] == 3:
                                        pass
                                    else:
                                        n_rv.add((nrx, nry))

                                    # 다음 갈 곳이 도착지라면 방문 처리하지 말기
                                    if maze[nbx][nby] == 4:
                                        pass
                                    else:
                                        n_bv.add((nbx, nby))

                                    q.append((nrx, nry, nbx, nby, cnt + 1, n_rv, n_bv))
    return 0