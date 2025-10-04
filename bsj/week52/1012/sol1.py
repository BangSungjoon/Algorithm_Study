# 유기농 배추
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

t = int(input())

for test_case in range(t):
    m, n, k = map(int, input().split())
    arr = [[0]*m for _ in range(n)]
    answer = 0

    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                dq = deque([(j, i)])
                arr[i][j] = 0
                while dq:
                    x, y = dq.popleft()

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if 0 <= nx < m and 0 <= ny < n and arr[ny][nx] == 1:
                            arr[ny][nx] = 0
                            dq.append((nx, ny))
                answer += 1

    print(answer)