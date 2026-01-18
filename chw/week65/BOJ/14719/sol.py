H, W = map(int, input().split())
block_info = map(int, input().split())

arr = [[0] * H for _ in range(W)]

for idx, block in enumerate(block_info):
    for j in range(block):
        arr[idx][H-j-1] = 1

# 현재 인덱스부터 빈 공간이 몇 개 있는지 탐색 -> 빈 공간이 아니면 막혔다고 체크 후 탈출
def water_count(i, j):
    is_blocked = False
    cnt = 0

    while i < W:
        if arr[i][j] == 1:
            is_blocked = True
            break
        else:
            cnt += 1

        i += 1

    return [is_blocked, cnt, i]

water = 0

# 맨 아래 행부터 탐색 -> 왼쪽이 막히고 빈 공간을 만났을 때 water_check
for j in range(H):
    j = H-j-1
    i = 0

    while i < W:
        if i < W-1:
            if arr[i][j] == 1 and arr[i+1][j] == 0:
                res = water_count(i+1, j)

                # 막혀서 물이 찰 수 있다면 water에 더해주기
                if res[0]:
                    water += res[1]

                # 탐색을 끝낸 인덱스로 바로 이동
                i = res[2]
                continue

        i += 1

print(water)