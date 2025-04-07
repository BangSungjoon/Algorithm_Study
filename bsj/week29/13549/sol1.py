# 숨바꼭질 3
import heapq

n, k = map(int, input().split())
visited = [0]*100001
q = []
heapq.heappush(q, (0, n))  # 이동 시간, 수빈이의 위치

while q:
    t, x = heapq.heappop(q)
    if x == k:
        print(t)
        break

    if visited[x]:
        # 어차피 시간 적게 드는 애들부터 방문했으니,
        # 이미 방문 했었다면 비교할 필요도 없이 pass
        continue
    visited[x] = 1

    if x < k and x*2 < 100001:
        heapq.heappush(q, (t, x*2))
    if x < k and x+1 < 100001:
        heapq.heappush(q, (t+1, x+1))
    if 0 < x:
        heapq.heappush(q, (t+1, x-1))