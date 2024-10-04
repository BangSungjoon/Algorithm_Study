# [SWEA] 1249. 보급로
## 풀이과정
1. DFS로 접근, 시간초과로 BFS로 풀이 변경
2. BFS로 만든 풀이가 정답과 달라 다시 DFS로 접근
3. 해결한 풀이들의 공통점이 지나온 경로의 비용을 기록한다는 점을 발견
4. 해당 풀이로 변경 후 통과
## 의문점
1. 똑같은 완전 탐색에 최소 경로를 찾는게 아니라 최소 비용을 찾는건데 <BR>DFS와 BFS가 실행시간이 차이나는 이유
2. BFS로 풀이 했을 때 정답을 제대로 못찾는 이유
3. 지나온 경로의 비용을 기록했을 때 시간이 절약되는 이유
### BFS 풀이 (실패)
```
# 1249. [S/W 문제해결 응용] 4일차 - 보급로
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    global min_cnt, n
    q = deque([(0, 0, 0)])

    # 탐색
    while q:
        x, y, cnt = q.popleft()
        if cnt >= min_cnt:  # 가지치기
            continue

        if x == n-1 and y == n-1:   # 목적지에 도착했다면
            min_cnt = cnt
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                q.append((nx, ny, cnt+int(arr[ny][nx])))

T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    arr = [input() for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    min_cnt = float('inf')
    visited[0][0] = 1
    bfs()

    print(f'#{test_case} {min_cnt}')
```