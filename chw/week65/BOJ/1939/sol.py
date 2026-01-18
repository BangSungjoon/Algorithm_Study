from heapq import heappush, heappop

N, M = map(int, input().split())

islands = [[] for _ in range(N+1)]

for _ in range(M):
    info = list(map(int, input().split()))
    islands[info[0]].append((info[1], info[2]))     # 연결된 섬, 제한 중량
    islands[info[1]].append((info[0], info[2]))

start, end = map(int, input().split())

weight = [0] * (N+1)  # start에서 각 섬까지 갈 때 최대 중량
weight[start] = int(1e9)

q = []
heappush(q, (-int(1e9), start))      # 최대 힙 사용

while q:
    w, now = heappop(q)
    w = -w                  # 양수로 다시 바꿔 주기

    # 현재까지 들고 온 중량이 이전에 경로로 갔을 때 중량보다 작으면 갱신 X
    if weight[now] > w:
        continue

    # 도착 섬이 나오면 그게 최대 중량임
    if now == end:
        print(w)
        break

    # 해당 섬과 연결된 섬을 확인해서 지금까지 들고 온 중량과 다음 섬에 가져갈 수 있는 중량 중 작은 걸 찾고
    # 그게 지금까지 기록한 최대 중량보다 크면 이 경로로 갱신
    for next_island, next_weight in islands[now]:
        possible_weight = min(w, next_weight)

        if weight[next_island] < possible_weight:
            weight[next_island] = possible_weight
            heappush(q, (-possible_weight, next_island))