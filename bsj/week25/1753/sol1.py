import heapq

v, e = map(int, input().split())    # v: 정점의 개수, e: 간선의 개수
k = int(input().strip())            # 시작 정점의 번호
adj_l = [[] for _ in range(v+1)]

for _ in range(e):
    a, b, weight = map(int, input().split())
    # a에서 b로 가는 가중치 weight인 간선 추가
    adj_l[a].append((b, weight))

INF = float('inf')
distance = [INF] * (v+1)
distance[k] = 0

# (현재 거리, 정점) 형태로 우선순위 큐에 삽입
hq = [(0, k)]

while hq:
    dist, current = heapq.heappop(hq)
    # 이미 더 짧은 경로가 있다면 무시
    if distance[current] < dist:
        continue
    # 인접 노드 확인
    for next_node, weight in adj_l[current]:
        new_dist = dist + weight
        if new_dist < distance[next_node]:
            distance[next_node] = new_dist
            # 우선순위 큐(최소 힙) heapq는 첫 번째 원소인 new_dist 기준으로 정렬 (물론 new_dist 값들이 같다면 next_node 기준으로 정렬)
            # 최소 값 우선
            heapq.heappush(hq, (new_dist, next_node))

for i in range(1, v+1):
    if distance[i] == float('inf'):
        print('INF')
    else:
        print(distance[i])