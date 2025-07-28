n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
y, x = 0, 0 # 아기 상어의 현재 위치(초기값)

# 아기 상어 위치 찾기
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            y, x = i, j
            arr[i][j] = 0

size = 2    # 아기 상어의 크기
time = 0    # 물고기 찾으러 돌아 댕긴 시간
fish = 0    # 물고기를 먹은 횟수
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

while True:
    q = [] # 아기 상어가 갈 수 있는 좌표
    visited = [[0]*n for _ in range(n)]
    visited[y][x] = 1  # 현재 아기 상어의 위치는 방문처리
    candidates = []     # 위치 우선도가 있기 때문에 먹이 후보군
    min_dist = None

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and visited[ny][nx] != 1 and arr[ny][nx] <= size:
            visited[ny][nx] = 1
            q.append((ny, nx, 1, arr[ny][nx]))

    while q:
        y, x, distance, fish_size = q.pop(0)
        if min_dist is not None and distance > min_dist:
            # 더 먼 칸은 볼 필요도 없음;
            break

        if 0 < fish_size < size:
            # 먹을 수 있어?
            candidates.append((distance, y, x))
            min_dist = distance # 최초 먹이 발견 시 거리 기록
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[ny][nx] != 1 and arr[ny][nx] <= size:
                visited[ny][nx] = 1
                q.append((ny, nx, distance + 1, arr[ny][nx]))

    if candidates:
        candidates.sort()
        dist, ny, nx = candidates[0]
        time += dist
        fish += 1
        arr[ny][nx] = 0
        y, x = ny, nx
        if fish == size:
            size += 1
            fish = 0
    else:
        print(time)
        break