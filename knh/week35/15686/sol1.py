# [G5] 15686 치킨 배달

from itertools import combinations

# STEP 1. 입력 받기
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# STEP 2. 집, 치킨 위치 넣기
homes = []
stores = []
result = 99999

for r in range(N):
    for c in range(N):
        if arr[r][c] == 1:
            homes.append((r,c))
        elif arr[r][c] == 2:
            stores.append((r, c))

# STEP 3. M개의 치킨집
for store in combinations(stores, M):
    tmp = 0
    for home in homes:
        length = 99999
        for i in range(M):
            length = min(length, abs(home[0]-store[i][0]) + abs(home[1]-store[i][1]))
        tmp += length
    result = min(result, tmp)

print(result)