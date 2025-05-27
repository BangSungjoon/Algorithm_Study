import sys, copy
input = sys.stdin.readline
from itertools import combinations

n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

houses = []
chickens = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            houses.append((i, j))
        elif arr[i][j] == 2:
            chickens.append((i, j))

min_total = sys.maxsize

for comb in combinations(chickens, m):
    total = 0
    for hx, hy in houses:    # 모든 집의 좌표를 하나씩 꺼내서
        min_dist = sys.maxsize   # 해당 집에서 치킨집까지의 최소 거리를 무한대로 초기화
        for cx, cy in comb:    # 선택된 치킨집 각각에 대해
            dist = abs(hx - cx) + abs(hy - cy) # 집과 치킨집 사이 거리
            min_dist = min(min_dist, dist)
        total += min_dist                      # 해당 집의 최소 거리를 도시 치킨거리 합계에 더함
    if total < min_total:   # 현재 조합의 도시 치킨 거리가 최소값보다 작으면
        min_total = total



print(min_total)  # 최소 도시 치킨 거리 출력