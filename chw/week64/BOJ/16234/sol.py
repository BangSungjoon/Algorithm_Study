from collections import deque

N, L, R = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(N)]


n = 0

while True:
    changed = False
    visited = [[0] * N for _ in range(N)]

    for y in range(N):
        for x in range(N):
            if not visited[x][y]:
                visited[x][y] = 1
                q = deque([(x, y)])
                association = [(x, y)]
                num = country[x][y]

                while q:
                    cx, cy = q.popleft()

                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx = cx + dx
                        ny = cy + dy

                        if (0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0
                                and L <= abs(country[cx][cy] - country[nx][ny]) <= R):
                            q.append((nx, ny))
                            association.append((nx, ny))
                            visited[nx][ny] = 1
                            num += country[nx][ny]

                if len(association) > 1:
                    changed = True
                    association_num = num // len(association)

                    for i, j in association:
                        country[i][j] = association_num

    if not changed:
        break

    n += 1

print(n)