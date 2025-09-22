from heapq import heappush, heappop

N = int(input())
M = int(input())
bus_info = [list(map(int, input().split())) for _ in range(M)]  # 출발 번호, 도착 번호, 비용
start, end = map(int, input().split())

graph = [[] for _ in range(N+1)]    # 버스 비용 기록
distance = [1e9] * (N+1)            # 최단 비용 기록

for info in bus_info:
    graph[info[0]].append((info[1], info[2]))   # (도착 도시, 비용)

def dijkstra(start):
    q = []
    heappush(q, (0, start))
    distance[start] = 0

    while q:
        cost, current = heappop(q)

        if distance[current] < cost:
            continue

        for g in graph[current]:
            new_cost = cost + g[1]

            if distance[g[0]] > new_cost:
                distance[g[0]] = new_cost
                heappush(q, (new_cost, g[0]))

dijkstra(start)

print(distance[end])


