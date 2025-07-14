import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
city_map = [list(map(int, input().split())) for _ in range(N)]

chicken = []
house = []
for i in range(N):
    for j in range(N):
        if city_map[i][j] == 2:
            chicken.append((i, j))

        if city_map[i][j] == 1:
            house.append((i, j))

chicken_from_house_list = []   # 각 집에서부터 모든 치킨집까지의 거리를 미리 계산

for x, y in house:
    dist_list = []

    for a, b in chicken:
        dist = abs(x-a) + abs(y-b)
        dist_list.append(dist)

    chicken_from_house_list.append(dist_list)

# 치킨 거리 계산
def calc_dist_of_chicken(survived_chicken_idx):
    dist_of_chicken = 0

    # 미리 계산해둔 각 치킨집까지 거리에서 살아남은 치킨집 index만 비교해서 최솟값 찾기
    for chicken_from_house in chicken_from_house_list:
        min_dist = float('inf')

        for i in survived_chicken_idx:
            min_dist = min(min_dist, chicken_from_house[i])

        dist_of_chicken += min_dist

    return dist_of_chicken

ans = float('inf')

for k in range(M, 0, -1):
    # 최대 k개 치킨집이 살아 남았을 경우 가능한 조합
    survived_chicken_list = list(combinations(range(len(chicken)), k))

    # 각 치킨집 조합마다 치킨 거리 계산 후 최솟값 찾기
    for survived_chicken_idx in survived_chicken_list:
        ans = min(ans, calc_dist_of_chicken(survived_chicken_idx))

print(ans)