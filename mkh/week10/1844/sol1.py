from collections import deque

deltas = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def solution(maps):
    N = len(maps)
    M = len(maps[0])
    dq = deque()
    dq.append((N-1,M-1,1))
    while dq:
        y, x, depth = dq.popleft()
        if y == 0 and x == 0:
            return depth
        for dy, dx in deltas:
            ny, nx = y+dy, x+dx
            if 0 <= ny < N and 0 <= nx < M and maps[ny][nx]:
                dq.append((ny, nx, depth + 1))
                maps[ny][nx] = 0
    return -1
