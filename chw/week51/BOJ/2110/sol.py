N, C = map(int, input().split())

houses = [int(input()) for _ in range(N)]
houses.sort()

# 가장 인접한 거리 범위
start = 1
end = houses[-1] - houses[0]

max_dist = 0

while start <= end:
    mid = (start + end) // 2    # 가장 인접한 거리

    cnt = 1
    current = houses[0]

    # 공유기 설치 - 해당 집에 설치했을 때 가장 인접한 거리 만큼 뺀 좌표가 curent 좌표보다 크거나 같아야 함 -> 그래야 설치 가능
    for i in range(1, N):
        if houses[i] - mid >= current:
            cnt += 1
            current = houses[i]     # 설치 체크

    if cnt >= C:
        start = mid + 1
        max_dist = mid
    else:
        end = mid - 1

print(max_dist)