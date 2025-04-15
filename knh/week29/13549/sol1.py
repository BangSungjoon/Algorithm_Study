# [G5] 13549 숨바꼭질 3

from collections import deque

N, K = map(int, input().split())   # 시작 위치 N, 목표 위치 K
limit = 100001                     # 좌표 범위 제한 (0 ~ 100000)
time = [0] * limit                 # 각 위치까지의 최소 시간 저장 배열

def bfs(x, y):
    q = deque()
    
    # 시작 위치가 0이면, 0에서는 순간이동 불가능하므로 1부터 시작
    if x == 0:
        q.append(1)
    else:
        q.append(x)
    
    while q:
        x = q.popleft()
        
        # 도착 지점에 도달하면 현재 시간 반환
        if y == x:
            return time[x]
        
        for nx in (x - 1, x + 1, x * 2):   # 이동 가능한 3가지 경우
            if 0 <= nx < limit and time[nx] == 0:
                if nx == 2 * x:            # 순간이동 (0초 소요)
                    time[nx] = time[x]
                    q.appendleft(nx)      # 가중치가 0이므로 앞에 삽입
                else:                     # 걷기 (1초 소요)
                    time[nx] = time[x] + 1
                    q.append(nx)          # 뒤에 삽입

# 시작점이 0일 때 예외 처리
if N == 0:
    if K == 0:
        print(0)
    else:
        print(bfs(N, K) + 1)  # 0에서는 순간이동 못하니까 +1 필요
else:
    print(bfs(N, K))          # 일반적인 경우
