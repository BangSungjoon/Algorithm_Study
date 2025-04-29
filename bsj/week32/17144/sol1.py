# 입력 받기
r, c, t = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(r)]

# 공기청정기 위치 찾기 (첫 열에 -1인 두 행)
purifier = []
for i in range(r):
    if room[i][0] == -1:
        purifier.append(i)
up = purifier[0]    # 위쪽 공기청정기 행
down = purifier[1]  # 아래쪽 공기청정기 행

# 확산 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(t):
    # 1) 미세먼지 확산
    d_room = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if room[i][j] > 0:
                amount = room[i][j] // 5
                for d in range(4):
                    ni = i + dx[d]
                    nj = j + dy[d]
                    # 범위 안 & 공기청정기 아니면 확산
                    if 0 <= ni < r and 0 <= nj < c and room[ni][nj] != -1:
                        d_room[ni][nj] += amount
                        room[i][j] -= amount
    # 확산된 양 합산
    for i in range(r):
        for j in range(c):
            room[i][j] += d_room[i][j]

    # 2) 공기청정기 작동
    # 위쪽 (반시계 방향)
    # 아래로
    for i in range(up-1, 0, -1):
        room[i][0] = room[i-1][0]
    # 왼쪽으로
    for j in range(c-1):
        room[0][j] = room[0][j+1]
    # 위로
    for i in range(up):
        room[i][c-1] = room[i+1][c-1]
    # 오른쪽으로
    for j in range(c-1, 1, -1):
        room[up][j] = room[up][j-1]
    room[up][1] = 0  # 공기청정기 바로 오른쪽은 깨끗한 공기

    # 아래쪽 (시계 방향)
    # 위로
    for i in range(down+1, r-1):
        room[i][0] = room[i+1][0]
    # 왼쪽으로
    for j in range(c-1):
        room[r-1][j] = room[r-1][j+1]
    # 아래로
    for i in range(r-1, down, -1):
        room[i][c-1] = room[i-1][c-1]
    # 오른쪽으로
    for j in range(c-1, 1, -1):
        room[down][j] = room[down][j-1]
    room[down][1] = 0  # 공기청정기 바로 오른쪽은 깨끗한 공기

# 남은 미세먼지 총합 계산
answer = 0
for i in range(r):
    for j in range(c):
        if room[i][j] > 0:
            answer += room[i][j]

print(answer)