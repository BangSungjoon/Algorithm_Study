import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().split())

res = 1e9
q = deque([(N, 0)])
visited = [0] * 100001
visited[N] = 1

while q:
    x, cnt = q.popleft()

    if x == K:
        res = min(res, cnt)

    for nx in [x-1, x+1, x*2]:
        if 0 <= nx <= 100000 and visited[nx] == 0:
            if nx == x * 2:
                visited[nx] = 1
                q.appendleft((nx, cnt))

            else:
                visited[nx] = 1
                q.append((nx, cnt+1))
print(res)