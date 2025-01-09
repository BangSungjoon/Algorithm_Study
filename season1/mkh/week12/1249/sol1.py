deltas = ((1, 0), (0, 1), (-1, 0), (0, -1))


def dfs(y, x, costs):
    global min_cost, visited
    if costs > min_cost:
        return
    elif y == x == N-1:
        min_cost = costs
    else:
        for dy, dx in deltas:
            ny, nx = y+dy, x+dx
            if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] > costs+roads[ny][nx]:
                visited[ny][nx] = costs+roads[ny][nx]
                dfs(ny, nx, costs+roads[ny][nx])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    roads = [list(map(int,list(input()))) for _ in range(N)]
    min_cost = float('inf')
    visited = [[100000]*N for _ in range(N)]
    dfs(0, 0, 0)
    print(f'#{tc} {min_cost}')