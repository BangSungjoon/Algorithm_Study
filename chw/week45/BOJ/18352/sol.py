import heapq

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    # A에서 B로 가는 비용은 1
    graph[A].append((B, 1))

distance = [1e9] * (N+1)
visited = [0] * (N+1)

q = []
heapq.heappush(q, (0, X))       # 거리 기준으로 최소힙
distance[X] = 0
visited[X] = 1

while q:
    dist, current = heapq.heappop(q)

    if distance[current] < dist:
        continue

    for i, c in graph[current]:
        cost = dist + c

        if cost < distance[i]:
            distance[i] = cost
            heapq.heappush(q, (cost, i))

possible_cities = []
for idx, d in enumerate(distance):
    if d == K:
        possible_cities.append(idx)

if possible_cities:
    for city in possible_cities:
        print(city)
else:
    print(-1)