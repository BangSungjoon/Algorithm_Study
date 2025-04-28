def clean_air(room, air_cleaner):
    top = air_cleaner[0]  # 공기청정기 위쪽 행
    bottom = air_cleaner[1]  # 공기청정기 아래쪽 행

    # 위쪽 공기청정기의 순환
    # 첫 번째 열
    for i in range(top - 1, 0, -1):
        room[i][0] = room[i - 1][0]
    # 첫 번째 행
    for i in range(0, C - 1):
        room[0][i] = room[0][i + 1]
    # 마지막 열
    for i in range(0, top):
        room[i][C - 1] = room[i + 1][C - 1]
    # 공기청정기 행
    for i in range(C - 1, 1, -1):
        room[top][i] = room[top][i - 1]
    room[top][1] = 0

    # 아래쪽 공기청정기의 순환
    # 첫 번째 열
    for i in range(bottom + 1, R - 1):
        room[i][0] = room[i + 1][0]
    # 마지막 행
    for i in range(0, C - 1):
        room[R - 1][i] = room[R - 1][i + 1]
    # 마지막 열
    for i in range(R - 1, bottom, -1):
        room[i][C - 1] = room[i - 1][C - 1]
    # 공기청정기 행
    for i in range(C - 1, 1, -1):
        room[bottom][i] = room[bottom][i - 1]
    room[bottom][1] = 0

    return room


def spread(room):
    next_room = [[0] * C for _ in range(R)]

    # 공기청정기 위치 복사
    for i in range(R):
        if room[i][0] == -1:
            next_room[i][0] = -1

    # 미세먼지 확산
    for i in range(R):
        for j in range(C):
            if room[i][j] > 0:
                dust = room[i][j]
                spread_amount = dust // 5
                spread_count = 0

                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < R and 0 <= nj < C and room[ni][nj] != -1:
                        next_room[ni][nj] += spread_amount
                        spread_count += 1

                # 현재 위치에 남은 미세먼지 더하기
                next_room[i][j] += dust - (spread_amount * spread_count)

    return next_room

R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]

# 공기청정기 위치 찾기
air_cleaner = []
for i in range(R):
    if room[i][0] == -1:
        air_cleaner.append(i)
        if len(air_cleaner) == 2:
            break

for t in range(T):
    # 1. 미세먼지 확산
    room = spread(room)
    # 2. 공기청정기 작동
    room = clean_air(room, air_cleaner)

res = 0
for r in range(R):
    for c in range(C):
        if room[r][c] != -1 and room[r][c] != 0:
            res += room[r][c]
print(res)